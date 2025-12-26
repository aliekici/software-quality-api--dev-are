from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str  

class User(UserBase):
    id: int
    class Config:
        from_attributes = True


class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None 
    price: float
    stock: int = 0  
    category_id: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    class Config:
        from_attributes = True


class ReviewBase(BaseModel):
    content: str
    rating: int
    product_id: int

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    class Config:
        from_attributes = True


class OrderItemBase(BaseModel):
    product_id: int
    quantity: int

class OrderItem(OrderItemBase):
    id: int
    class Config:
        from_attributes = True

class OrderCreate(BaseModel):
    user_id: int
    items: List[OrderItemBase] 

class Order(BaseModel):
    id: int
    user_id: int
    items: List[OrderItem]
    class Config:
        from_attributes = True