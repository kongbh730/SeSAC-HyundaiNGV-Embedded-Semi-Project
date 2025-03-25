#Central Control Unit
import RPi.GPIO as GPIO
import time
import can
import isotp
import serial

# Web post import
import requests 

# GPIO 핀 설정 (BCM 번호)
TRIG_PIN = 23
ECHO_PIN = 24
VIBRATION_PIN = 16

# CAN 설정
CAN_CHANNEL = 'can0'
DISTANCE_CAN_ID = 0x100
VIBRATION_CAN_ID = 0x200

# UART 설정 (ttyS0, 9600 baudrate)
uart1 = serial.Serial('/dev/ttyS0', 9600, timeout=1)
uart2 = serial.Serial('/dev/ttyAMA3', 9600, timeout=1)
uart3 = serial.Serial('/dev/ttyAMA5', 9600, timeout=1)
uart4 = serial.Serial('/dev/ttyAMA2', 9600, timeout=1)

def measure_distance():
    GPIO.output(TRIG_PIN, False)
    time.sleep(0.002)

    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    pulse_start = time.time()
    pulse_end = time.time()
    timeout = time.time() + 0.04

    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()
        if pulse_start > timeout:
            return None

    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()
        if pulse_end > timeout:
            return None

    duration = pulse_end - pulse_start
    distance_cm = round((duration * 34300) / 2)
    return distance_cm

def process_uds_request(payload):
    """
    수신된 UDS 요청 메시지를 해석하여 적절한 응답을 생성합니다.
    - 0x10 0x03: 확장 진단 세션 요청 → 긍정 응답: 0x50 0x03
    - 0x19 0x02: DTC 요청 → 긍정 응답: 0x59 + (P1A00: 0x1A, 0x00)
    그 외는 Negative Response (0x7F, 요청 서비스 ID, 오류 코드)로 응답합니다.
    """
    if len(payload) < 2:
        print("유효하지 않은 UDS 요청 길이")
        return None

    service_id = payload[0]
    sub_function = payload[1]

    if service_id == 0x10:  # Diagnostic Session Control
        if sub_function == 0x03:
            print("UDS: 확장 진단 세션 요청 수신")
            return bytes([0x50, sub_function])
        else:
            print(f"UDS: 지원하지 않는 세션 서브펑션: {hex(sub_function)}")
            return bytes([0x7F, service_id, 0x12])
    elif service_id == 0x19:  # Read DTC Information
        if sub_function == 0x02:
            print("UDS: DTC 요청 수신")
            # P1A00 (제조사별 코드) - 충돌에 의한 파워트레인 손상
            return bytes([0x59, 0x1A, 0x00])
        else:
            print(f"UDS: 지원하지 않는 DTC 서브펑션: {hex(sub_function)}")
            return bytes([0x7F, service_id, 0x12])
    else:
        print(f"UDS: 알 수 없는 서비스 ID: {hex(service_id)}")
        return bytes([0x7F, service_id, 0x11])
        
# Web post function
def send_to_server(vehicle_id, distance, vibration):
    try:
        payload = {
            "vehicleId": vehicle_id,
            "distance": distance,
            "vibration": vibration
        }
        response = requests.post("http://192.168.100.122:8081/api/can", json=payload)
        print(f"[POST 전송] 상태 전송 완료 (status {response.status_code})")
    except Exception as e:
        print(f"[POST 실패] {e}")


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)
    GPIO.setup(VIBRATION_PIN, GPIO.IN)

    # CAN 버스 초기화 (센서용과 UDS용 모두 동일한 버스 사용)
    bus = can.interface.Bus(channel=CAN_CHANNEL, interface='socketcan')

    # UDS용 ISO-TP 스택 설정
    # 클라이언트는 요청 시 0x7DF로 전송하므로, 서버는 rxid=0x7DF, 응답은 txid=0x7C4로 전송합니다.
    uds_address = isotp.Address(isotp.AddressingMode.Normal_11bits, rxid=0x7DF, txid=0x7C4)
    uds_stack = isotp.CanStack(bus=bus, address=uds_address)

    print("초음파/진동 센서와 UDS 서버 시작 (Ctrl+C 종료)")

    sensor_interval = 0.5      # 센서 데이터 전송 간격 (초)
    last_sensor_time = time.time()

    try:
        while True:
            # UDS 요청 처리 (빈번하게 폴링)
            uds_stack.process()
            uds_payload = uds_stack.recv()
            if uds_payload is not None:
                print("UDS 요청 수신:", uds_payload.hex())
                uds_response = process_uds_request(uds_payload)
                if uds_response:
                    uds_stack.send(uds_response)
                    print("UDS 응답 전송:", uds_response.hex())

            # 센서 관련 작업은 주기적으로 실행
            now = time.time()
            if now - last_sensor_time >= sensor_interval:
                last_sensor_time = now

                # 초음파 센서 측정
                distance = measure_distance()
                if distance is not None:
                    distance_int = int(distance)
                    distance_data = [(distance_int >> 8) & 0xFF, distance_int & 0xFF]
                    distance_msg = can.Message(arbitration_id=DISTANCE_CAN_ID,
                                               data=distance_data,
                                               is_extended_id=False)
                    bus.send(distance_msg)
                    print(f"[CAN 0x100] 거리: {distance_int} cm")

                    # 초음파 거리 5cm 미만이면 UART로 '1' 전송
                    if distance_int < 5:
                        data = b'1'
                        uart1.write(data)
                        uart2.write(data)
                        uart3.write(data)
                        uart4.write(data)
                        print("[UART] '1' 전송 (거리 5cm 미만)")
                else:
                    print("거리 측정 실패")

                # 진동 센서 상태 (LOW = 충돌 감지) 확인 및 CAN 메시지 전송
                vibration_detected = GPIO.input(VIBRATION_PIN) == GPIO.LOW
                vibration_data = [0x01] if vibration_detected else [0x00]
                vibration_msg = can.Message(arbitration_id=VIBRATION_CAN_ID,
                                            data=vibration_data,
                                            is_extended_id=False)
                bus.send(vibration_msg)
                print(f"[CAN 0x200] 진동 상태: {'충돌 감지' if vibration_detected else '정상'}")

                # 충돌 감지 시 UART로 '0' 전송
                if vibration_detected:
                    data = b'0'
                    uart1.write(data)
                    uart2.write(data)
                    uart3.write(data)
                    uart4.write(data)
                    print("[UART] '0' 전송 (충돌 감지)")
                    
                    # 서버 전송 함수 수행
                    send_to_server(vehicle_id=1, distance=-1, vibration=True)
			        
            # 짧은 딜레이 (UDS와 센서 처리를 위해 폴링 주기를 짧게 함)
            time.sleep(0.01)

    except KeyboardInterrupt:
        print("종료합니다.")
    finally:
        GPIO.cleanup()
        uart1.close()
        uart2.close()
        uart3.close()
        uart4.close()
        uds_stack.shutdown()
        print("프로그램 종료.")

if __name__ == "__main__":
    main()
