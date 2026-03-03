from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "flight-ingestion-service"
    api_v1_prefix: str = "/api/v1"
    aviationstack_base_url: str = "http://api.aviationstack.com/v1"
    aviationstack_api_key: str = ""
    kafka_bootstrap_servers: str = "kafka:9092"
    kafka_topic_flight_updates: str = "flight_updates"
    jwt_secret: str = "change-me"
    jwt_algorithm: str = "HS256"

    class Config:
        env_file = ".env"


settings = Settings()
