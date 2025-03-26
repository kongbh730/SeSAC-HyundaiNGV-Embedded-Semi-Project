<h1>🚘 현대자동차그룹 모빌리티 SW 개발자 데뷔 과정</h1>
<h2>🔧 중간 프로젝트</h2>
<h2><a href="http://192.168.100.122:8081/vehicleViewer.html">사고 모니터링 웹 서비스 : 미배포</h2>
<p>📅 <strong>진행 기간:</strong> 2025-03-18 ~ 2025-03-27</p>

<img src="https://github.com/user-attachments/assets/b1219eef-5cc7-4096-b62d-ff7fa889b284" alt="중간 프로젝트 플로우차트 버스" style="width: 100%; max-width: 600px;">
<h2>🎬 프로젝트 시연 영상</h2>

[![Video Label](http://img.youtube.com/vi/6gstFbx9MVY/0.jpg)](https://youtu.be/6gstFbx9MVY)

<hr>
<h2>👨‍👩‍👦‍👦 팀원 소개</h2>
<table width="1000">
  <tbody>
    <tr>
      <td width="25%" align="center">
        <a href="https://github.com/jihosky">
          <img src="https://github.com/jihosky.png" style="width: 90%; border-radius: 50%;">
        </a>
      </td>
      <td width="25%" align="center">
        <a href="https://github.com/kongbh730">
          <img src="https://github.com/kongbh730.png" style="width: 90%; border-radius: 50%;">
        </a>
      </td>
      <td width="25%" align="center">
        <a href="https://github.com/Do-Yeop-Kim">
          <img src="https://github.com/Do-Yeop-Kim.png" style="width: 90%; border-radius: 50%;">
        </a>
      </td>
      <td width="25%" align="center">
        <a href="https://github.com/jin05105">
          <img src="https://github.com/jin05105.png" style="width: 90%; border-radius: 50%;">
        </a>
      </td>
    </tr>
    <tr>
      <td align="center">
        <a href="https://github.com/jihosky">문지호<br>@jihosky</a>
      </td>
      <td align="center">
        <a href="https://github.com/kongbh730">공병현<br>@kongbh730</a>
      </td>
      <td align="center">
        <a href="https://github.com/Do-Yeop-Kim">김도엽<br>@Do-Yeop-Kim</a>
      </td>
      <td align="center">
        <a href="https://github.com/jin05105">이태규<br>@jin05105</a>
      </td>
    </tr>
    <tr>
      <td align="center">
        프로젝트 매니지먼트<br>아키텍처 설계<br>CAN, UART, UDS 통신 구축 및 테스팅
      </td>
      <td align="center">
        부저, LED 모듈 개발<br>웹 서비스 구축<br>산출물 관리
      </td>
      <td align="center">
        엔코더 모터<br>서보 모터 모듈 개발
      </td>
      <td align="center">
        LCD 모듈 개발<br>요구사항 분석 및 테스트 케이스 작성
      </td>
    </tr>
  </tbody>
</table>

<hr>
<h2>📁 코드 구조 및 설명</h2>
<ul>
  <li><strong>📄 <a href="https://github.com/kongbh730/SeSAC-HyundaiNGV-Embedded-Semi-Project/blob/main/CANtoWebGateway.py">RaspiCAN.py</strong> – 라즈베리파이 CAN 통신 및 사고 감지 스크립트</a></li>
  <li><strong>📄 <a href="https://github.com/kongbh730/SeSAC-HyundaiNGV-Embedded-Semi-Project/blob/main/RaspiCAN.py">CANtoWebGateway.py</strong> – 라즈베리파이 CAN-Web 통신 스크립트</a></li>
  <li><strong>📁 <a href="https://github.com/kongbh730/SeSAC-HyundaiNGV-Embedded-Semi-Project/tree/main/LCD">LCD/</strong> – LCD 디스플레이 제어</a>
    <ul>
      <li>📁 Core/</li>
      <li>📁 Drivers/</li>
      <li>📁 MDK-ARM/</li>
      <li>LCD.ioc</li>
    </ul>
  </li>
  <li><strong>📁 <a href="https://github.com/kongbh730/SeSAC-HyundaiNGV-Embedded-Semi-Project/tree/main/MotorControl">MotorControl/</strong> – DC 모터 제어</a>
    <ul>
      <li>📁 Core/</li>
      <li>📁 Drivers/</li>
      <li>📁 MDK-ARM/</li>
      <li>motor.ioc</li>
    </ul>
  </li>
  <li><strong>📁 <a href="https://github.com/kongbh730/SeSAC-HyundaiNGV-Embedded-Semi-Project/tree/main/ServoMotorControl">ServoMotorControl/</strong> – 서보모터 제어</a>
    <ul>
      <li>📁 Core/</li>
      <li>📁 Drivers/</li>
      <li>📁 MDK-ARM/</li>
      <li>Servo_Motor.ioc</li>
    </ul>
  </li>
  <li><strong>📁 <a href="https://github.com/kongbh730/SeSAC-HyundaiNGV-Embedded-Semi-Project/tree/main/Buzzer">Buzzer/</strong> – 부저 (경고음) 제어트</a>
    <ul>
      <li>📁 Core/</li>
      <li>📁 Drivers/</li>
      <li>📁 MDK-ARM/</li>
      <li>SeSAC_semi_project.ioc</li>
    </ul>
  </li>
  <li><strong>📁 <a href="https://github.com/kongbh730/SeSAC-HyundaiNGV-Embedded-Semi-Project/tree/main/WebService">WebService/</strong> – Spring Boot 웹 서비스 (DB, WebSocket 실시간 알림)</a>
    <ul>
      <li>📁 src/ – 자바 소스코드</li>
      <li>build.gradle – Gradle 설정</li>
    </ul>
  </li>
</ul>

<hr>
<h2>🛠 사용 장비</h2>

<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th>분류</th>
      <th>장비</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>MCU</strong></td>
      <td>STM32 Nucleo-L073RZ, Raspberry Pi 4</td>
    </tr>
    <tr>
      <td><strong>통신</strong></td>
      <td>CAN, UART</td>
    </tr>
    <tr>
      <td><strong>센서</strong></td>
      <td>SW-420 진동 감지 센서, HC-SR04 초음파 센서</td>
    </tr>
    <tr>
      <td><strong>쉴드</strong></td>
      <td>WEKIT LCD 1602 쉴드, 아두이노 모터 쉴드 Rev 3, DHT11 이지 모듈 쉴드</td>
    </tr>
    <tr>
      <td><strong>모터</strong></td>
      <td>SG90-HV 서보모터, MB-2832E 엔코더 모터</td>
    </tr>
  </tbody>
</table>

