from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserLogin
from app.auth.password_hash import hash_password, verify_password
from app.auth.jwt_handler import create_access_token

auth_router = APIRouter(tags=["Auth"])

# ---------------- Register ----------------
@auth_router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    # Check if userid already exists
    user_exists = db.query(User).filter(User.userid == user.userid).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="User ID already exists")

    email_exists = db.query(User).filter(User.email == user.email).first()
    if email_exists:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        fullname=user.fullname,
        userid=user.userid,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}

# ---------------- Login ----------------
@auth_router.post("/login")
def login(credentials: UserLogin, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.userid == credentials.userid).first()
    if not user:
        raise HTTPException(status_code=404, detail="Invalid User ID")

    if not verify_password(credentials.password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect Password")

    token = create_access_token({"userid": user.userid})

    return {"message": "Login successful", "access_token": token}
