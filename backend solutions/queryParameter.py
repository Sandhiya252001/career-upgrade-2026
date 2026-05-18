from fastapi import FastAPI
app=FastAPI()
products=[]
@app.get('/add')
def add(a:int,b:int):
    return{"Result":a+b}

    
