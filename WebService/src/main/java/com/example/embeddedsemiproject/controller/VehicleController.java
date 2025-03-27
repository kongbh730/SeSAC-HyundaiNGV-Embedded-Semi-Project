package com.example.embeddedsemiproject.controller;

import com.example.embeddedsemiproject.dto.VehicleDTO;
import com.example.embeddedsemiproject.service.VehicleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api")
public class VehicleController {

    @Autowired
    private VehicleService vehicleService;

    @GetMapping("/vehicles")
    public List<VehicleDTO> getVehicles() {
        return vehicleService.getAllVehicles();
    }

    // VehicleController.java
    @PostMapping("/vehicles/reset-status")
    public ResponseEntity<Void> resetAllVehicleStatus() {
        vehicleService.resetAllStatus();
        return ResponseEntity.ok().build();
    }

}
