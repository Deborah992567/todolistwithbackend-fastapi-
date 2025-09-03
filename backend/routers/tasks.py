from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import date

import schemas
from models import Task, User
from database import get_db
from auth import get_current_user

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# --- Get all tasks for logged-in user ---
@router.get("/", response_model=List[schemas.Task])
def get_tasks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Task).filter(Task.user_id == current_user.id).all()

# --- Create task ---
@router.post("/", response_model=schemas.Task, status_code=status.HTTP_201_CREATED)
def create_task(payload: schemas.TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = Task(
        title=payload.title,
        description=payload.description,
        importance=payload.importance,
        due_date=payload.due_date,
        completed=False,
        user_id=current_user.id  # ✅ fixed
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

# --- Update task ---
@router.put("/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, payload: schemas.TaskUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    update_data = payload.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task

# --- Delete task ---
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return

# --- Summary endpoint ---
@router.get("/summary")
def summarize_tasks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    tasks = db.query(Task).filter(Task.user_id == current_user.id).all()

    total = len(tasks)
    completed = sum(1 for t in tasks if t.completed)
    pending = total - completed
    overdue = sum(1 for t in tasks if t.due_date and t.due_date < date.today() and not t.completed)

    importance_counts = {
        "important": sum(1 for t in tasks if t.importance == "important"),
        "mid": sum(1 for t in tasks if t.importance == "mid"),
        "unimportant": sum(1 for t in tasks if t.importance == "unimportant"),
    }

    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "overdue": overdue,
        "importance": importance_counts,
    }
