package com.aerostream.graphql;

import com.aerostream.model.FlightKpi;
import com.aerostream.service.AnalyticsService;
import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

import java.util.List;

@Controller
public class AnalyticsGraphqlController {
    private final AnalyticsService service;

    public AnalyticsGraphqlController(AnalyticsService service) { this.service = service; }

    @QueryMapping
    public List<FlightKpi> analyticsByFlight(@Argument String flightNumber) {
        return service.getByFlight(flightNumber);
    }
}
