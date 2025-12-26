from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models, schemas

router = APIRouter()

@router.post("/", response_model=schemas.Product, status_code=201)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
 
    cat = db.query(models.Category).filter(models.Category.id == product.category_id).first()
    if not cat:
        raise HTTPException(status_code=404, detail="Category not found")
    
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/", response_model=List[schemas.Product])
def read_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()