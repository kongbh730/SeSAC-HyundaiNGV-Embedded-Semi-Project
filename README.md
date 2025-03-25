<h1>🚘 현대자동차그룹 모빌리티 SW 개발자 데뷔 과정</h1>
<h2>🔧 중간 프로젝트</h2>
<p>📅 <strong>진행 기간:</strong> 2025-03-18 ~ 2025-03-27</p>

<img src="https://github.com/user-attachments/assets/b1219eef-5cc7-4096-b62d-ff7fa889b284" alt="중간 프로젝트 플로우차트 버스" style="width: 100%; max-width: 600px;">

<hr>
<h2>👨‍👩‍👦‍👦 팀원 소개</h2>
<table>
  <tbody>
    <tr>
      <td>
        <a href="https://github.com/jihosky">
          <img src="https://github.com/jihosky.png" width="200" style="border-radius: 50%;">
        </a>
      </td>
      <td>
        <a href="https://github.com/kongbh730">
          <img src="https://github.com/kongbh730.png" width="200" style="border-radius: 50%;">
        </a>
      </td>
      <td>
        <a href="https://github.com/Do-Yeop-Kim">
          <img src="https://github.com/Do-Yeop-Kim.png" width="200" style="border-radius: 50%;">
        </a>
      </td>
      <td>
        <a href="https://github.com/jin05105">
          <img src="https://github.com/jin05105.png" width="200" style="border-radius: 50%;">
        </a>
      </td>
    </tr>
    <tr>
      <td align="center"><a href="https://github.com/jihosky">문지호@jihosky</a></td>
      <td align="center"><a href="https://github.com/kongbh730">공병현@kongbh730</a></td>
      <td align="center"><a href="https://github.com/Do-Yeop-Kim">김도엽@Do-Yeop-Kim</a></td>
      <td align="center"><a href="https://github.com/jin05105">이태규@jin05105</a></td>
    </tr>
    <tr>
      <td>CAN 통신 구축,...</td>
      <td>WebService 구현,...</td>
      <td>Motor 기능 구현,...</td>
      <td>LCD 기능 구현,...</td>
    </tr>
  </tbody>
</table>

<h2>👨‍💻 팀원 소개</h2>

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/jihosky">
        <img src="https://github.com/jihosky.png" width="100" style="border-radius: 50%;"><br>
        <strong>문지호</strong><br>
        @jihosky
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/kongbh730">
        <img src="https://github.com/kongbh730.png" width="100" style="border-radius: 50%;"><br>
        <strong>공병현</strong><br>
        @kongbh730
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Do-Yeop-Kim">
        <img src="https://github.com/Do-Yeop-Kim.png" width="100" style="border-radius: 50%;"><br>
        <strong>김도엽</strong><br>
        @Do-Yeop-Kim
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/jin05105">
        <img src="https://github.com/jin05105.png" width="100" style="border-radius: 50%;"><br>
        <strong>이태규</strong><br>
        @jin05105
      </a>
    </td>
  </tr>
</table>


<hr>
<h2>📁 코드 구조 및 설명</h2>
<ul>
  <li><strong>📄 RaspiCAN.py</strong> – 라즈베리파이 CAN 통신 및 사고 감지 스크립트</li>
  <li><strong>📁 LCD/</strong> – LCD 디스플레이 제어</li>
  <li><strong>📁 Motor/</strong> – DC 모터 제어</li>
  <li><strong>📁 Motor/ServoMotor/</strong> – 서보모터 제어</li>
  <li><strong>📁 Buzzer/</strong> – 부저 (경고음) 제어</li>
  <li><strong>📁 WebService/</strong> – Spring Boot 웹 서비스 (DB, WebSocket 실시간 알림)
    <ul>
      <li>src/ – 자바 소스코드</li>
      <li>build.gradle – Gradle 설정</li>
      <li>application.yml – 환경 설정</li>
    </ul>
  </li>
</ul>
