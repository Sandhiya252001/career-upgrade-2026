from fastapi import FastAPI
app=FastAPI()
err=[]
@app.get("/logs/{level}")
def getErrLogs(level:str):
    with open(r"C:\Users\sandhiya.c.subramani\Desktop\Python\Day 01\career_upgrade_2026\backend solutions\sampleLog.log") as f:
        line=f.readlines()
        for i in line:
            if level=="ERROR" and "ERROR" in i:
                r=i
                err.append(r)
    return{"ERROR LOGS":err}
 
    