from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from routers import users, tasks, ai

# Create tables (dev only; use Alembic in prod)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ToDo SaaS API", version="1.0.0")

# CORS - adjust for your frontend origin(s)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(tasks.router)
app.include_router(ai.router)

@app.get("/")
def root():
    return {"ok": True, "service": "todo-api"}
