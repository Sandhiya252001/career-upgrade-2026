from fastapi import FastAPI

app = FastAPI()

@app.get("/logs")
def read_logs():
    count_error = 0
    count_info = 0
    count_warn = 0

    with open("sampleLog.log", "r") as f:
        for line in f:
            if "INFO" in line:
                count_info += 1
            elif "ERROR" in line:
                count_error += 1
            elif "WARNING" in line:
                count_warn += 1

    return {
        "INFO": count_info,
        "ERROR": count_error,
        "WARNING": count_warn
    }
