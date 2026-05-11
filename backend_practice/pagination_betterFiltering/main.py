from database import base,engine,SessionLocal
from models import Logs
from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
import auth
import schema
base.metadata.create_all(bind=engine)
app=FastAPI()
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/add-logs',dependencies=[Depends(auth.verify_key)])
def add_logs(log:schema.LogCreate,db:Session=Depends(get_db)):
    db=SessionLocal()
    new_log=Logs(level=log.level,message=log.message)
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    db.close()
    return{"message":"Log added successfully","data":new_log.id}
@app.get('/logs')
def get_logs(level:str=None,
             skip:int=0,
             limit:int=2,
             db:Session=Depends(get_db)):
    query=db.query(Logs)

    if level:
        query=query.filter(Logs.level==level)
    logs=query.offset(skip).limit(limit).all()
    return logs


