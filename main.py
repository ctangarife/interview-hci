#main.py
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.api.routes.transcription import router as transcription_router
from markupsafe import Markup

app = FastAPI(title="Interview Transcription Service")

# Mount static files
app.mount("/static", StaticFiles(directory="interview/static"), name="static")

# Configure templates
templates = Jinja2Templates(directory="interview/templates")

# Include transcription API router
app.include_router(transcription_router, prefix="/api")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "user_input": ""})

@app.post("/submit-form")
async def handle_form(request: Request):
    form_data = await request.form()
    user_text = form_data.get("user_text", "")
    # XSS Vulnerability! Rendering input directly without sanitization
    return templates.TemplateResponse("index.html", {"request": request, "user_input": Markup(user_text)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, reload_dirs=["interview"])