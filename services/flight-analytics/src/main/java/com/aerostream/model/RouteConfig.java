package com.aerostream.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "route_config")
public class RouteConfig {
    @Id
    private String id;
    private String routeKey;
    private Integer delayThreshold;

    public String getId() { return id; }
    public String getRouteKey() { return routeKey; }
    public void setRouteKey(String routeKey) { this.routeKey = routeKey; }
    public Integer getDelayThreshold() { return delayThreshold; }
    public void setDelayThreshold(Integer delayThreshold) { this.delayThreshold = delayThreshold; }
}
