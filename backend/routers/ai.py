from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from auth import get_current_user
import models

router = APIRouter(prefix="/ai", tags=["AI"])

# Request model
class ExplainRequest(BaseModel):
    text: str

@router.post("/explain")
def explain_task(req: ExplainRequest):
    """
    Simplify or explain a single task.
    (Later you can plug this into OpenAI/Anthropic for real AI.)
    """
    simplified = f"This task is about: {req.text[:80]}..."
    return {"original": req.text, "simplified": simplified}

@router.get("/summarize")
def summarize_tasks(db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    """
    Summarize all tasks for the logged-in user.
    """
    tasks = db.query(models.Task).filter(models.Task.owner_id == user.id).all()
    if not tasks:
        return {"summary": "No tasks found."}

    # Fake AI summarization (replace with real LLM later)
    titles = [t.title for t in tasks]
    summary = f"You have {len(tasks)} tasks. Examples: {', '.join(titles[:5])}..."
    return {"summary": summary}
