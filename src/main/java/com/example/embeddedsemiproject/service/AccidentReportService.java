package com.example.embeddedsemiproject.service;

import com.example.embeddedsemiproject.dao.AccidentReportDAO;
import com.example.embeddedsemiproject.dto.AccidentReportDTO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class AccidentReportService {

    @Autowired
    private AccidentReportDAO accidentReportDAO;

    public List<AccidentReportDTO> getAllAccidents() {
        return accidentReportDAO.findAll();
    }
}
