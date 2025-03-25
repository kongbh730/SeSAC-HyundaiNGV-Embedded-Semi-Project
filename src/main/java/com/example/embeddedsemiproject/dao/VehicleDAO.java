package com.example.embeddedsemiproject.dao;

import com.example.embeddedsemiproject.dto.VehicleDTO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public class VehicleDAO {

    @Autowired
    private JdbcTemplate jdbcTemplate;

    public List<VehicleDTO> findAll() {
        String sql = "SELECT * FROM Vehicles";
        return jdbcTemplate.query(sql, (rs, rowNum) -> {
            VehicleDTO v = new VehicleDTO();
            v.setId(rs.getInt("id"));
            v.setName(rs.getString("name"));
            v.setStatus(rs.getString("status"));
            v.setDriver(rs.getString("driver"));
            v.setLocation(rs.getString("location"));
            return v;
        });
    }

    public void updateStatus(int id, String status) {
        String sql = "UPDATE Vehicles SET status = ? WHERE id = ?";
        jdbcTemplate.update(sql, status, id);
    }
}
