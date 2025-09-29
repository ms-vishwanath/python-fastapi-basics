from fastapi import FastAPI
app = FastAPI()
products = [
        {"id": 1, "name": "Product 1"},
        {"id": 2, "name": "Product 2"},
        {"id": 3, "name": "Product 3"},
]

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/products")
def read_products():
    print(products)
    return {"products": products}

@app.post("/")
def create_product(data:dict):
    print(data)
    return {"message": "Data has been recieved"}

