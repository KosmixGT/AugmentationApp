from typing import List

from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db

from user.schemas import UserSchema, CreateUserSchema
import user.crud as crud

router = APIRouter(prefix='/users', tags=['user'])

@router.get("/{user_login}", response_model=UserSchema)
async def get_user_by_login(user_login: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_login(db, login=user_login)
    if not db_user:
        raise HTTPException(status_code=400, detail="User does not exist")
    return db_user

#CREATE A USER
@router.post("/register/", response_model=UserSchema)
async def add_user(user: CreateUserSchema, db: Session = Depends(get_db)):
    # checking if username already exists 
    user_exists = crud.get_user_by_login(db=db, login=user.login)
    if user_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
        detail="Userlogin already exists")
    
    return crud.create_user(user=user, db=db)