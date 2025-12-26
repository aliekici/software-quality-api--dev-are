from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models, schemas

router = APIRouter()

@router.post("/", response_model=schemas.Review, status_code=201)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    prod = db.query(models.Product).filter(models.Product.id == review.product_id).first()
    if not prod:
         raise HTTPException(status_code=404, detail="Product not found")
    
    db_review = models.Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

@router.get("/", response_model=List[schemas.Review])
def read_reviews(db: Session = Depends(get_db)):
    return db.query(models.Review).all()    