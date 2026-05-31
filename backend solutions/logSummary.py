from fastapi import FastAPI
app=FastAPI()
@app.get('/log-summary')
def getSummary():
    err = 0
    inf = 0
    warn = 0

    with open(r"C:\Users\sandhiya.c.subramani\Desktop\Python\Day 01\career_upgrade_2026\python_concepts\Automation\sample.log") as f:
        lines = f.readlines()
        for line in lines:
            if "ERROR" in line:
                err += 1
            if "WARNING" in line:
                warn += 1
            if "INFO" in line:
                inf += 1
        count = len(lines)
        return{"total_logs": count,
  "errors": err,
  "warnings": warn}