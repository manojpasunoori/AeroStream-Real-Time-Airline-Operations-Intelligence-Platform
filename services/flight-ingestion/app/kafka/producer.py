import json
from confluent_kafka import Producer
from app.core.config import settings


class KafkaProducer:
    def __init__(self) -> None:
        self.producer = Producer({"bootstrap.servers": settings.kafka_bootstrap_servers})

    def publish(self, topic: str, payload: dict) -> None:
        self.producer.produce(topic, json.dumps(payload).encode("utf-8"))
        self.producer.flush()
