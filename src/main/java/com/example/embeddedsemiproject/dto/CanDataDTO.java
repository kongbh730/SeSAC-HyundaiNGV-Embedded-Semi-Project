package com.example.embeddedsemiproject.dto;

import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class CanDataDTO {
    private int vehicleId;
    private int distance;
    private boolean vibration;

    // Getter/Setter 생략 가능 (롬복 쓰면 @Data)
    @Override
    public String toString() {
        return "vehicleId=" + vehicleId + ", distance=" + distance + ", vibration=" + vibration;
    }

}
