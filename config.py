import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Secret key for Flask sessions
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")

    # Get database URL from environment
    DATABASE_URL = os.environ.get("DATABASE_URL")

    # Render sometimes gives postgres:// instead of postgresql://
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

    # Use Render PostgreSQL in production, SQLite locally
    SQLALCHEMY_DATABASE_URI = DATABASE_URL or "sqlite:///site.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False