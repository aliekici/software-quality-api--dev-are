from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models, schemas

router = APIRouter()

@router.post("/", response_model=schemas.Category, status_code=201)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):

    existing_cat = db.query(models.Category).filter(models.Category.name == category.name).first()
    

    if existing_cat:
        raise HTTPException(status_code=400, detail="Category already exists")

    db_cat = models.Category(name=category.name)
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat

@router.get("/", response_model=List[schemas.Category])
def read_categories(db: Session = Depends(get_db)):
    return db.query(models.Category).all()