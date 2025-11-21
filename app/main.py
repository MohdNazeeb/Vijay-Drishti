from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database import Base, engine
from app.auth.auth_router import auth_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Mount static folder
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Template folder
templates = Jinja2Templates(directory="app/templates")

# Include API routes
app.include_router(auth_router)

# -----------------------------------
# FRONTEND PAGE ROUTES (RENDER HTML)
# -----------------------------------

@app.get("/")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/dashboard")
def dashboard_page(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
