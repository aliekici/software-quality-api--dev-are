from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter()

@router.post("/", response_model=schemas.Order, status_code=201)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
  
    user = db.query(models.User).filter(models.User.id == order.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
  
    db_order = models.Order(user_id=order.user_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    
  
    for item in order.items:
        product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
        if not product:
            continue
        
        db_item = models.OrderItem(
            order_id=db_order.id,
            product_id=item.product_id,
            quantity=item.quantity
        )
        db.add(db_item)
    
    db.commit()
    db.refresh(db_order)
    return db_order