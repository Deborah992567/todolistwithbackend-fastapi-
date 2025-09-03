from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    tasks = relationship("Task", back_populates="owner", cascade="all, delete-orphan")


class Task(Base):
   __tablename__ = "tasks"
   id = Column(Integer, primary_key=True, index=True)
   title = Column(String, nullable=False)
   description = Column(String, nullable=True)
   importance = Column(String, default="mid")  # "important", "mid", "unimportant"completed = Column(Boolean, default=False)
   due_date = Column(Date, nullable=True)
   owner_id = Column(Integer, ForeignKey("users.id"))
   owner = relationship("User", back_populates="tasks")