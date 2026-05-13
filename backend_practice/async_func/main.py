from fastapi import FastAPI,Depends,HTTPException
from database import SessionLocal,engine,Base
import schemas
import auth
from model import logClass
from sqlalchemy.orm import Session
import logging
import asyncio
Base.metadata.create_all(bind=engine)
app=FastAPI()
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post('/add-logs',dependencies=[Depends(auth.verifyKey)])
async def add_log(log:schemas.Logger,db:Session=Depends(get_db)):
    try:
        await asyncio.sleep(1)
        new_log=logClass(level=log.level,message=log.message)
        db.add(new_log)
        db.commit()
        db.refresh(new_log)
        logging.info("Log Added")
        return{"message":"Log Added Successfully","data":new_log.id}
    except Exception as e:
        logging.error("Failed to add log")
        raise HTTPException(status_code=500,detail="Something went wrong")
@app.get('/get_logs')
async def get_logs(db:Session=Depends(get_db)):
    try:
        await asyncio.sleep(1)
        logs=db.query(logClass).all()
        return logs
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    

    
    