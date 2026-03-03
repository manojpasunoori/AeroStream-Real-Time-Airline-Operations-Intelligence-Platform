package com.aerostream.kafka;

import com.aerostream.service.AnalyticsService;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

import java.util.Map;

@Component
public class FlightEventConsumer {
    private final AnalyticsService analyticsService;

    public FlightEventConsumer(AnalyticsService analyticsService) { this.analyticsService = analyticsService; }

    @KafkaListener(topics = "flight_updates", groupId = "flight-analytics")
    public void consume(Map<String, Object> payload) {
        String flightNumber = (String) payload.getOrDefault("flight_number", "UNKNOWN");
        String routeKey = (String) payload.getOrDefault("route_key", "UNK-UNK");
        Integer delay = (Integer) payload.getOrDefault("delay_minutes", 0);
        String status = (String) payload.getOrDefault("status", "unknown");
        analyticsService.processEvent(flightNumber, routeKey, delay, status);
    }
}
