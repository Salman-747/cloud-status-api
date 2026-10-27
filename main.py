from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="Cloud Status API",
    description="A simple application for learning cloud deployment",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Cloud Status API is running!",
        "status": "online"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.get("/info")
def application_info():
    return {
        "application": "Cloud Status API",
        "version": "1.0.0",
        "environment": "development"
    }