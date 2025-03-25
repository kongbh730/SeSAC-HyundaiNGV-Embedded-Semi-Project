package com.example.embeddedsemiproject.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class AccidentReportDTO {
    private int id;
    private String datetime;
    private String location;
    private int vehicleId;

    // Getters and Setters
}
