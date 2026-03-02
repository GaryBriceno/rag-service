from fastapi import FastAPI
from app.api.v1.routes_health import router as health_router

app = FastAPI(title="rag-service")
app.include_router(health_router, prefix="/v1")