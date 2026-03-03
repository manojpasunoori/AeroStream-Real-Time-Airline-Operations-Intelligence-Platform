package com.aerostream.controller;

import com.aerostream.model.FlightKpi;
import com.aerostream.service.AnalyticsService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/analytics")
public class AnalyticsController {
    private final AnalyticsService service;

    public AnalyticsController(AnalyticsService service) { this.service = service; }

    @GetMapping
    public List<FlightKpi> all() { return service.getAll(); }

    @GetMapping("/flight/{flightNumber}")
    public List<FlightKpi> byFlight(@PathVariable String flightNumber) {
        return service.getByFlight(flightNumber);
    }

    @GetMapping("/route/{routeKey}")
    public List<FlightKpi> byRoute(@PathVariable String routeKey) {
        return service.getByRoute(routeKey);
    }
}
