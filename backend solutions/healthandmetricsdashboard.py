from fastapi import FastAPI
app=FastAPI()
@app.get('/dashboard')
def getDetails():
    err=0
    inf=0
    warn=0
    with open(r"C:\Users\sandhiya.c.subramani\Desktop\Python\Day 01\career_upgrade_2026\backend solutions\sampleLog.log") as f:
        lines=f.readlines()
        for i in lines:
            if "ERROR" in i:
                err+=1
            if "WARNING" in i:
                warn+=1
        total_logs=len(i)
        return{"status":"healthy",
  "total_logs":total_logs,
  "errors":err,
  "warnings":warn}
    