from sqlalchemy.orm import Session
from models import User
from user.schemas import UserSchema, CreateUserSchema
from fastapi import HTTPException, status

def get_user_by_login(db: Session, login: str):
    return db.query(User).filter(User.login == login).first()

def create_user(db: Session, user: UserSchema):
    db_user = User(name=user.login, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user