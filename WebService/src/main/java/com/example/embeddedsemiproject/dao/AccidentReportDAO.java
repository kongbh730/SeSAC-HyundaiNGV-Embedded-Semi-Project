package com.example.embeddedsemiproject.dao;

import com.example.embeddedsemiproject.dto.AccidentReportDTO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.time.LocalDateTime;
import java.util.List;

// com.example.monitoring.dao.AccidentDAO.java
@Repository
public class AccidentReportDAO {

    @Autowired
    private JdbcTemplate jdbcTemplate;

    public List<AccidentReportDTO> findAll() {
        String sql = "SELECT * FROM AccidentReports ORDER BY datetime DESC";

        return jdbcTemplate.query(sql, (rs, rowNum) -> {
            AccidentReportDTO accident = new AccidentReportDTO();
            accident.setId(rs.getInt("id"));
            accident.setDatetime(rs.getString("datetime"));
            accident.setLocation(rs.getString("location"));
            accident.setVehicleId(rs.getInt("vehicle_id"));
            return accident;
        });
    }

    public void insertAccidentReport(int vehicleId, String location) {
        String sql = "INSERT INTO AccidentReports (vehicle_id, location, datetime) VALUES (?, ?, ?)";
        jdbcTemplate.update(sql, vehicleId, location, LocalDateTime.now());
    }
}
