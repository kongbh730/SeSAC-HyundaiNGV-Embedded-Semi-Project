package com.example.embeddedsemiproject.service;

import com.example.embeddedsemiproject.dao.VehicleDAO;
import com.example.embeddedsemiproject.dto.VehicleDTO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class VehicleService {

    @Autowired
    private VehicleDAO vehicleDAO;

    public List<VehicleDTO> getAllVehicles() {
        return vehicleDAO.findAll();
    }
}
