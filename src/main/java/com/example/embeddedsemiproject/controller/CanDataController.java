package com.example.embeddedsemiproject.controller;

import com.example.embeddedsemiproject.dao.AccidentReportDAO;
import com.example.embeddedsemiproject.dao.VehicleDAO;
import com.example.embeddedsemiproject.dto.CanDataDTO;
import com.example.embeddedsemiproject.websocket.AccidentWebSocketHandler;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDateTime;

@RestController
@RequestMapping("/api")
public class CanDataController {

    @Autowired
    private VehicleDAO vehicleDAO;

    @Autowired
    private AccidentReportDAO accidentReportDAO;

    @Autowired
    private AccidentWebSocketHandler webSocketHandler;


    // 마지막 사고 기록 시간 저장 (차량별로 관리하고 싶으면 Map<Integer, LocalDateTime>으로)
    private LocalDateTime lastAccidentTime = LocalDateTime.MIN;

    private static final int ACCIDENT_COOLDOWN_SECONDS = 10; // 10초 쿨타임

    @PostMapping("/can")
    public String receiveCanData(@RequestBody CanDataDTO data) {
        LocalDateTime now = LocalDateTime.now();

        System.out.println("수신된 CAN 데이터:");
        System.out.println("수신 시간: " + now);
        System.out.println("데이터: " + data);

        if (data.isVibration()) {
            if (lastAccidentTime.plusSeconds(ACCIDENT_COOLDOWN_SECONDS).isBefore(now)) {
                vehicleDAO.updateStatus(data.getVehicleId(), "Accident Reported");

                // WebSocket 브로드캐스트
                //webSocketHandler.broadcast("ALERT:" + data.getVehicleId());
                webSocketHandler.broadcast("accident:" + data.getVehicleId());

                String location = "자동 감지 위치"; // 또는 vehicleDAO.findLocationById()
                accidentReportDAO.insertAccidentReport(data.getVehicleId(), location);

                lastAccidentTime = now;
                System.out.println("사고 기록 추가됨 (" + now + ")");
            } else {
                System.out.println("중복 사고 기록 방지됨 (쿨타임 미충족)");
            }
        }

        return "success";
    }
}
