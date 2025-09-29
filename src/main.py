from fastapi import FastAPI
from fastapi import Request
from fastapi import HTTPException
app = FastAPI()


products=[
    {"id": 1, "name": "Product 1", "price": 100},
    {"id": 2, "name": "Product 2", "price": 200},
    {"id": 3, "name": "Product 3", "price": 300},
    {"id": 4, "name": "Product 4", "price": 300},
    {"id": 5, "name": "Product 5", "price": 300},
]

# health check 
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# read products
@app.get("/products")
def read_products(request: Request):
    query = request.query_params
    searchQuery = query.get("search")
    results = products
    if searchQuery:
        results = [product for product in products if searchQuery in product.get("name","")]
    return {"products": results}

# add product
@app.post("/products")
def add_product(product: dict):
    data = product.get("data")
    products.append({
        "id": len(products) + 1,
        "name": data.get("name"),
        "price": data.get("price"),
    })
    return {"message": "Product has been added"}

# delete product
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for product in products:
        if product.get("id") == product_id:
            products.remove(product)
            break
    return {"message": "Product has been deleted"}

