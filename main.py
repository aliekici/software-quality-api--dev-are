from fastapi import FastAPI
from database import engine, Base
from routes import users, products, categories, orders, reviews


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Final Project API",
    description="Software Quality & Test Project",
    version="1.0.0"
)

app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(categories.router, prefix="/api/categories", tags=["Categories"])
app.include_router(products.router, prefix="/api/products", tags=["Products"])
app.include_router(orders.router, prefix="/api/orders", tags=["Orders"])
app.include_router(reviews.router, prefix="/api/reviews", tags=["Reviews"])

@app.get("/")
def root():
    return {"message": "API is running. Go to /docs for Swagger."}