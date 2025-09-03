from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL

engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
Base = declarative_base()

# ⚠️ Do NOT drop/create inside here, it will reset DB on every run!
# Only use Base.metadata.create_all(bind=engine) during initial setup

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
