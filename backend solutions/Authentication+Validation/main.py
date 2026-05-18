from database import engine, SessionLocal, base
from models import Log
from fastapi import FastAPI, HTTPException, Depends
import schemas
import auth
import time

base.metadata.create_all(bind=engine)

app = FastAPI()
cache={}
TTL=10

# =========================
# DB Dependency
# =========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =========================
# CREATE (Protected)
# =========================
@app.post('/create-logs', dependencies=[Depends(auth.verify_api_key)])
def create_logs(log: schemas.LogCreate, db=Depends(get_db)):
    new_log = Log(level=log.level, message=log.message)
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return {"message": "Log added", "data": new_log.id}

# =========================
# GET ALL (Public)
# =========================
@app.get("/get-logs")
def get_logs(db=Depends(get_db)):
    return db.query(Log).all()

# =========================
# GET BY ID (Public)
# =========================
# @app.get("/getlogs/{id}")
# def getLogsbyid(id: int, db=Depends(get_db)):
#     now=time.time()
#     if id in cache:
#         print("CACHE HIT")
#         return cache[id]
#     print("chache miss")

#     log = db.query(Log).filter(Log.id == id).first()

#     if not log:
#         raise HTTPException(status_code=404, detail="Log not found")
#     cache[id] = log

#     return log
@app.get("/logs/{id}")
def get_log(id: int, db=Depends(get_db)):

    # 1️⃣ Check cache
    if id in cache:
        print("CACHE HIT")
        return cache[id]

    # 2️⃣ Cache miss → fetch from DB
    print("CACHE MISS")
    log = db.query(Log).filter(Log.id == id).first()

    if not log:
        raise HTTPException(status_code=404, detail="Log not found")

    # 3️⃣ Store in cache
    cache[id] = log

    #return log
    #return {"source": db}
    return {"source": cache}

# =========================
# UPDATE (Protected)
# =========================
@app.put("/update-log/{id}", dependencies=[Depends(auth.verify_api_key)])
def change_log(id: int, log: schemas.LogCreate, db=Depends(get_db)):
    logs = db.query(Log).filter(Log.id == id).first()

    if not logs:
        raise HTTPException(status_code=404, detail="Log not found")

    logs.level = log.level
    logs.message = log.message

    db.commit()
    db.refresh(logs)

    return {"message": "Log Updated"}

# =========================
# DELETE (Protected)
# =========================
@app.delete("/delete/{id}", dependencies=[Depends(auth.verify_api_key)])
def remove_log(id: int, db=Depends(get_db)):
    logg = db.query(Log).filter(Log.id == id).first()

    if not logg:
        raise HTTPException(status_code=404, detail="Log not found")

    db.delete(logg)
    db.commit()

    return {"message": "Log deleted"}