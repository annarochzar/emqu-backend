# app/schemas/user.py
from pydantic import BaseModel, EmailStr, constr

class UserCreate(BaseModel):
    name: constr(min_length=1)
    email: EmailStr
    password: constr(min_length=6)
