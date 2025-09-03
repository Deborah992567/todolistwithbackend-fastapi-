# reset_db.py
from database import engine, Base
from models import User, Task  # ✅ import your models so they register with Base

print("🚨 Dropping all tables...")
Base.metadata.drop_all(bind=engine)

print("✅ Creating all tables fresh...")
Base.metadata.create_all(bind=engine)

print("🎉 Database reset complete!")
