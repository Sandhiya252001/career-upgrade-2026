from fastapi import FastAPI
app=FastAPI()
with open("sampleLog.log","r") as f:
        file=f.readlines()
@app.get('/logs')
def read_logs():
    return {"Data":file}
@app.get('/log-stats')
def count_logs():
    errorCount=0
    warnCount=0
    infoCount=0
    for i in file:
        if "ERROR" in i:
            errorCount+=1
        if "INFO" in i:
            infoCount+=1
        if "WARNING" in i:
            warnCount+=1
    return{"ERROR" : errorCount,
               "WARNING" : warnCount,
               "INFO" : infoCount}
            
    
    