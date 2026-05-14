from fastapi import FastAPI
from app.database import engine, Base
from app.routes.logs import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Log Analyzer API",
    version="1.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Log Analyzer API is running"
    }