#CAN to Web Gateway
import requests
import can

# ---------------------------------------------------------------------------
# 웹 서버 전송 함수
def send_to_server(vehicle_id, distance, vibration):
    try:
        payload = {
            "vehicleId": vehicle_id,
            "distance": distance,
            "vibration": vibration
        }
        print(f"[서버 전송 시도] payload: {payload}")
        response = requests.post("http://192.168.100.122:8081/api/can", json=payload)
        print(f"[POST 전송] 상태 전송 완료 (status {response.status_code})")
        print("[서버 응답]", response.text)
    except Exception as e:
        print(f"[POST 실패] {e}")

# ---------------------------------------------------------------------------
# CAN 메시지를 모니터링하여 조건에 맞으면 서버로 전송하는 함수
def monitor_can_messages():
    first_message = True  # 첫 메시지 여부 체크
    # 환경에 맞게 CAN 버스 초기화 (예: 채널 'can0', 인터페이스 'socketcan')
    bus = can.interface.Bus(channel='can0', interface='socketcan')
    
    while True:
        message = bus.recv()  # CAN 메시지 blocking 방식 수신
        # 수신한 모든 CAN 메시지 출력
        print(f"[CAN 수신] 메시지 수신됨: arbitration_id: {message.arbitration_id}, data: {message.data}")
        
        # CAN ID가 100인 메시지만 처리
        if message.arbitration_id == 0x100:
            current_value = message.data[0]
            # 첫 메시지라면 단순히 상태 출력 후 건너뜁니다.
            if first_message:
                first_message = False
                print("[DEBUG] 첫 메시지이므로 서버 전송을 하지 않습니다.")
                continue
            # 0번 데이터가 1(0x1)일 경우 서버로 전송
            if current_value == 0x1:
                print("[DEBUG] 조건 충족: CAN ID 100의 0번 데이터가 1입니다. 서버 전송을 시도합니다.")
                send_to_server(vehicle_id=1, distance=-1, vibration=True)
            else:
                print(f"[DEBUG] 조건 미충족: 0번 데이터 값은 {hex(current_value)} 입니다.")

# ---------------------------------------------------------------------------
if __name__ == "__main__":
    monitor_can_messages()
