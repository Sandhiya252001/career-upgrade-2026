from fastapi import FastAPI
app=FastAPI()
@app.get('/metrics')
def get_metrics():
    ERR = 0
    INF = 0
    WARN = 0

    with open("sampleLog.log", "r") as f:
        for line in f:
            if "ERROR" in line:
                ERR += 1
            if "INFO" in line:
                INF += 1
            if "WARNING" in line:
                WARN += 1
    return {"ERROR":ERR,"INFO":INF,"WARNING":WARN}





