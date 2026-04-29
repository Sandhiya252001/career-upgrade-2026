from fastapi import FastAPI
app=FastAPI()
keyword=""
@app.get('/search')
def searchLogs(keyword:str):
    result=[]
    with open('sampleLog.log') as f:
        file=f.readlines()
    for i in file:
        if keyword in i:
            result.append(i)
    return {"Result": result}

    