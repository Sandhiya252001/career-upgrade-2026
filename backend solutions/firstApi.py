from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return {"message" : "Hello API"}
@app.get("/user")
def user():
    return {"username" : "Sandhiya","email":"san@gmail.com"}
    