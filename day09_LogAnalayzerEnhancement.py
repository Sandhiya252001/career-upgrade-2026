from fastapi import FastAPI
app=FastAPI()
@app.get("/error-logs")
def get_errors():
    error=[]
    with open("sampleLog.log","r") as f:
        file=f.readlines()
    for i in file:
        if "ERROR" in i:
            error.append(i)
    return {"errors":error} 
