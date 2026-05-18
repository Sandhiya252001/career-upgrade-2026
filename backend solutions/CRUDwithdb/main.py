from database import engine, SessionLocal
from models import Log, Base
from fastapi import FastAPI, HTTPException

Base.metadata.create_all(bind=engine)

app = FastAPI()

# 🔹 CREATE
@app.post('/add-log')
def add_logs(level: str, message: str):
    if level not in ["INFO", "ERROR", "WARNING"]:
        raise HTTPException(status_code=400, detail="Invalid level")

    db = SessionLocal()
    new_log = Log(level=level, message=message)
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    db.close()

    return {"message": "Log added", "data": new_log.id}


# 🔹 GET ALL
@app.get('/get-logs')
def get_logs():
    db = SessionLocal()
    logs = db.query(Log).all()
    db.close()
    return logs


# 🔹 GET ONE
@app.get('/get-logs/{id}')
def get_log(id: int):
    db = SessionLocal()
    log = db.query(Log).filter(Log.id == id).first()
    db.close()

    if not log:
        raise HTTPException(status_code=404, detail="Log not found")

    return log


# 🔹 UPDATE
@app.put('/update-log/{id}')
def update_log(id: int, level: str, message: str):
    if level not in ["INFO", "ERROR", "WARNING"]:
        raise HTTPException(status_code=400, detail="Invalid level")

    db = SessionLocal()
    log = db.query(Log).filter(Log.id == id).first()

    if not log:
        db.close()
        raise HTTPException(status_code=404, detail="Log not found")

    log.level = level
    log.message = message

    db.commit()
    db.refresh(log)
    db.close()

    return {"message": "Log updated"}


# 🔹 DELETE
@app.delete('/delete-log/{id}')
def delete_log(id: int):
    db = SessionLocal()
    log = db.query(Log).filter(Log.id == id).first()

    if not log:
        db.close()
        raise HTTPException(status_code=404, detail="Log not found")

    db.delete(log)
    db.commit()
    db.close()

    return {"message": "Log deleted"}