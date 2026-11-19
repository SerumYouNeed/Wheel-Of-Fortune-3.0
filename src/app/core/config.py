import os

SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-secret-key-change-me-in-production-0123456789")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60