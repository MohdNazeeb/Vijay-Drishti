import jwt
from datetime import datetime, timedelta

SECRET_KEY = "Vijay_Drishti_Secret_Key_123"
ALGORITHM = "HS256"

def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode["exp"] = datetime.utcnow() + timedelta(hours=5)
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
