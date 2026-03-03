package com.aerostream.repository;

import com.aerostream.model.FlightKpi;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface FlightKpiRepository extends JpaRepository<FlightKpi, Long> {
    List<FlightKpi> findByFlightNumber(String flightNumber);
    List<FlightKpi> findByRouteKey(String routeKey);
}
