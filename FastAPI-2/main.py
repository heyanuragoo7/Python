from fastapi import FastAPI, HTTPException
from models import Product
from database import Session, engine
import database_models

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return {"message": "Hello, World!"}

products = [
    Product(id=1, name="Product-1", description="Desc-1", price=100, quantity=5),
    Product(id=2, name="Product-2", description="Desc-2", price=100, quantity=5)
]

def init_db():

    db = Session()
    count = db.query(database_models.Product).count

    if count == 0:
        for i in products:
            db.add(database_models.Product(**i.model_dump())) 
        db.commit()

init_db()

# @app.get("/products")
# def list_products():
#     return products

# DB
@app.get("/products")
def list_products():
    db = Session()
    db.query()
    return products


@app.get("/product/{id}")
def get_productbyid(id:int):
    return products[id-1]

@app.post("/product")
def create_data(data:Product):
    products.append(data)
    return products

@app.put("/product/{id}")
def update_product(id: int, data: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = data
            return "Done"
    return "Error happened!"

# @app.patch("/product/{id}")
# def update_product(id: int, data: Product):
#     for product in products:
#         if product.id == id:
#             if data.name is not None:
#                 product.name = data.name
#             if data.price is not None:
#                 product.price = data.price

#             return {"message": "Product updated", "product": product}

#     raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/product/{id}")
def remove_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Deleted"
    return "Not Found"