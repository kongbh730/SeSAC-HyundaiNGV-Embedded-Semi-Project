package com.example.embeddedsemiproject.controller;

import com.example.embeddedsemiproject.dto.AccidentReportDTO;
import com.example.embeddedsemiproject.service.AccidentReportService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api")
public class AccidentReportController {

    @Autowired
    private AccidentReportService accidentReportService;

    @GetMapping("/accidents")
    public List<AccidentReportDTO> getAllAccidents() {
        return accidentReportService.getAllAccidents();
    }
}
