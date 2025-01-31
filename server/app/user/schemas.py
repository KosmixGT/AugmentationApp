from typing import List, Optional, Generic, TypeVar

from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class UserSchema(BaseModel):
    login: str
    password: str

    class Config:
        orm_mode = True
        from_attributes = True


class CreateUserSchema(BaseModel):
    login: str
    password: str

    class Config:
        orm_mode = True
        from_attributes = True
