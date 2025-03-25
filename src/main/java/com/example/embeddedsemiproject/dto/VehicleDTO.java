package com.example.embeddedsemiproject.dto;

public class VehicleDTO {
    private int id;
    private String name;
    private String status;
    private String driver;
    private String location;

    // Getters and Setters
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }

    public String getStatus() {
        return status;
    }
    public void setStatus(String status) {
        this.status = status;
    }

    public String getDriver() {
        return driver;
    }
    public void setDriver(String driver) {
        this.driver = driver;
    }

    public String getLocation() {
        return location;
    }
    public void setLocation(String location) {
        this.location = location;
    }
}
