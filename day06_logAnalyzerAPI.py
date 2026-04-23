from fastapi import FastAPI

app = FastAPI()
print("Running log analyzer API")

@app.get("/")
def home():
    return {"message": "Server working"}

@app.get("/logs")
def readLogs():
    with open("sampleLog.log","r") as f:
        data = f.readlines()
    return {"Data": data}