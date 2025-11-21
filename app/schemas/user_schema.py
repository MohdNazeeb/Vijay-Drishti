from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    fullname: str
    userid: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    userid: str
    password: str

class UserResponse(BaseModel):
    id: int
    fullname: str
    userid: str
    email: str

    class Config:
        orm_mode = True
