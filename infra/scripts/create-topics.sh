#!/usr/bin/env bash
set -euo pipefail
kafka-topics --bootstrap-server kafka:9092 --create --if-not-exists --topic flight_updates --partitions 3 --replication-factor 1
kafka-topics --bootstrap-server kafka:9092 --create --if-not-exists --topic delay_events --partitions 3 --replication-factor 1
kafka-topics --bootstrap-server kafka:9092 --create --if-not-exists --topic route_performance --partitions 3 --replication-factor 1
