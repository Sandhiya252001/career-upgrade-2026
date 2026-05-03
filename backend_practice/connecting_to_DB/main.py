from database import engine
from models import Base
from fastapi import FastAPI
from database import SessionLocal
from models import Log
Base.metadata.create_all(bind=engine)
app=FastAPI()
@app.post('/add-log')
def add_log(level:str,message:str):
    db=SessionLocal()
    new_log=Log(level=level,message=message)
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    db.close()
    return{"Message":"Log Added","data":new_log.id}
@app.get('/get-logs')
def get_logs():
    db=SessionLocal()
    logs=db.query(Log).all()
    db.close
    return logs

