from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from strawberry.fastapi import GraphQLRouter
import strawberry

from app.api.routes import router
from app.core.config import settings


@strawberry.type
class Query:
    @strawberry.field
    def service_name(self) -> str:
        return settings.app_name


schema = strawberry.Schema(query=Query)

app = FastAPI(title="Flight Ingestion Service", version="1.0.0", openapi_url=f"{settings.api_v1_prefix}/openapi.json")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router, prefix=settings.api_v1_prefix)
app.include_router(GraphQLRouter(schema), prefix="/graphql")
Instrumentator().instrument(app).expose(app)
