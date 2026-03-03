package com.aerostream.repository;

import com.aerostream.model.RouteConfig;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.Optional;

public interface RouteConfigRepository extends MongoRepository<RouteConfig, String> {
    Optional<RouteConfig> findByRouteKey(String routeKey);
}
