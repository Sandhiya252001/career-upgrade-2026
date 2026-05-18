from database import Base,engine
from fastapi import FastAPI
from router import router
Base.metadata.create_all(bind=engine)
app=FastAPI()
app.include_router(router)
