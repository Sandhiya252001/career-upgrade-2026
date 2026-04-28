from fastapi import FastAPI

app = FastAPI()

@app.get("/square/{num}")
def square(num: int):
    return {"result": num * num}

numbers=[]
@app.post("/area/{num}")
def area(num: int):
    area = num * num
    data = {"Number":num,"Value":area}
    numbers.append(data)
    return {"message": "value stored", "data": data}
@app.get("/values")
def getValues():
    return {"Values" : numbers}


@app.put("/area/{value}/{num}")
def areaUpdate(value: int, num: int):
    area = num * num
    data = {"Number":num,"Value":area}
    numbers.append(data)
    return {"message": "value stored", "data": data}