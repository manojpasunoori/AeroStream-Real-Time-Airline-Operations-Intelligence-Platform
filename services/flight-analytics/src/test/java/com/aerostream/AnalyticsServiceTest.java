package com.aerostream;

import com.aerostream.model.FlightKpi;
import com.aerostream.repository.FlightKpiRepository;
import com.aerostream.service.AnalyticsService;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class AnalyticsServiceTest {
    @Test
    void reliabilityScoreShouldDecreaseWithDelay() {
        FlightKpiRepository repository = Mockito.mock(FlightKpiRepository.class);
        Mockito.when(repository.save(Mockito.any())).thenAnswer(i -> i.getArguments()[0]);
        AnalyticsService service = new AnalyticsService(repository);
        FlightKpi kpi = service.processEvent("AA100", "JFK-LAX", 20, "active");
        assertEquals(70.0, kpi.getReliabilityScore());
    }
}
