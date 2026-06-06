from fastapi import FastAPI
app=FastAPI()
@app.get('/export-metrics')
def getMetrics():
    Err=0
    warn=0
    with open(r"C:\Users\sandhiya.c.subramani\Desktop\Python\Day 01\career_upgrade_2026\python_concepts\Automation\sample.log") as f:
        line=f.readlines()
        for i in line:
            if "ERROR" in i:
                Err+=1
            if "WARNING" in i:
                warn+=1
    Total=len(line)
    if Total > 0:
        error_rate = ( Err/ Total) * 100
    else:
        error_rate = 0
    return {
    "Report": "Monitoring Report",
    "Total Logs": Total,
    "Errors": Err,
    "Warnings": warn,
    "Error Rate": error_rate
}
@app.post('/add-metrics')
def addMetrics(status:str):
    with open("metrics.txt","a") as f:
        f.write(str(getMetrics())+ "\n")
    return {"Message":"File added successfully"}


