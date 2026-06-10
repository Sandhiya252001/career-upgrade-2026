from fastapi import FastAPI
import time
import requests
app=FastAPI()
@app.get('/details')
def getDetails():
    start_time=time.time()
    url="https://google.com"
    response=requests.get(url)
    end_time=time.time()
    response_time=(end_time-start_time)*1000
    return{"Status":"UP",
           "Response Time":response_time}
 