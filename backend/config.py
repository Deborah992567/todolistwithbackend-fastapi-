import os
from datetime import timedelta

# keep it simple for dev; switch to env vars in prod
SECRET_KEY = os.getenv("SECRET_KEY", "dev-super-secret")  # change in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_MIN", "60"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_DAYS", "7"))

DATABASE_URL = os.getenv("DATABASE_URL", 'postgresql://neondb_owner:npg_FE5nCNQay1mg@ep-young-dew-adqfc9xa-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require')
