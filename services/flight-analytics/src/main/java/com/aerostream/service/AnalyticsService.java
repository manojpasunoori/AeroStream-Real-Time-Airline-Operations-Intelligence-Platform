package com.aerostream.service;

import com.aerostream.model.FlightKpi;
import com.aerostream.repository.FlightKpiRepository;
import org.springframework.stereotype.Service;

import java.time.Instant;
import java.util.List;

@Service
public class AnalyticsService {
    private final FlightKpiRepository repository;

    public AnalyticsService(FlightKpiRepository repository) { this.repository = repository; }

    public FlightKpi processEvent(String flightNumber, String routeKey, Integer delayMinutes, String status) {
        FlightKpi kpi = new FlightKpi();
        kpi.setFlightNumber(flightNumber);
        kpi.setRouteKey(routeKey);
        kpi.setDelayMinutes(delayMinutes);
        kpi.setStatus(status);
        kpi.setReliabilityScore(Math.max(0, 100 - (delayMinutes * 1.5)));
        kpi.setProcessedAt(Instant.now());
        return repository.save(kpi);
    }

    public List<FlightKpi> getByFlight(String flightNumber) { return repository.findByFlightNumber(flightNumber); }
    public List<FlightKpi> getByRoute(String routeKey) { return repository.findByRouteKey(routeKey); }
    public List<FlightKpi> getAll() { return repository.findAll(); }
}
