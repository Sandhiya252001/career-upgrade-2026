from fastapi import FastAPI
import time
import requests
app=FastAPI()
@app.get('/health')
def getHealth():
    return {"Status" : "Healthy"}
@app.get('/details')
def getResponseTime():
    url="http://127.0.0.1:8000/health"
    start_time = time.time()

    response = requests.get(url)

    end_time = time.time()

    response_time = (end_time - start_time) * 1000

    return{
  "response_time_ms":response_time}
