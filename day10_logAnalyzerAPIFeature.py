from fastapi import FastAPI
from collections import Counter

app = FastAPI()

LOG_FILE = "logs.txt"


@app.get("/log-summary")
def log_summary():
    
    counts = Counter()
    total_logs = 0

    with open("sampleLog.log", "r") as file:
        for line in file:
            total_logs += 1

            if "INFO" in line:
                counts["INFO"] += 1
            elif "ERROR" in line:
                counts["ERROR"] += 1
            elif "WARNING" in line:
                counts["WARNING"] += 1

    return {
        "total_logs": total_logs,
        "INFO": counts["INFO"],
        "ERROR": counts["ERROR"],
        "WARNING": counts["WARNING"]
    }