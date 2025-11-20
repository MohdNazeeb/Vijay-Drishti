# app/main.py

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="Vijay Drishti Backend",
    description="Backend for Vijay Drishti login/register + dashboard",
    version="0.1.0"
)

# Mount static files (css/js/images)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Setup templates directory
templates = Jinja2Templates(directory="app/templates")

# Root endpoint (just for testing)
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "title": "Login | Vijay Drishti"})

# Example dashboard endpoint (protected routes to be added later)
@app.get("/dashboard")
async def dashboard(request: Request):
    # TODO: add auth logic here
    return templates.TemplateResponse("dashboard.html", {"request": request, "title": "Dashboard | Vijay Drishti"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
