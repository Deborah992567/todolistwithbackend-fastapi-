from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

# --- Task Schemas ---
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    importance: Optional[str] = "mid"
    due_date: Optional[date] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    importance: Optional[str] = None
    completed: Optional[bool] = None
    due_date: Optional[date] = None

class Task(TaskBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True


# --- User Schemas ---
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):   # ✅ Add this for responses
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
     access_token: str
     refresh_token: str
     token_type: str = "bearer"
    