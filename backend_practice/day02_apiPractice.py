from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def info():
    return{"message":"hello world"}
@app.get("/users")
def user():
    return{"name" : "Sandhiya","email":"san@gmail.com","phno":"1234567890"}
@app.get("/products")
def product():
    productname="Phone"
    productbrand="Samsung"
    return{"Product":productname,"Brand":productbrand}

