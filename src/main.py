import sys
from fastapi import FastAPI,Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from .routers import sanitize
app = FastAPI()

app.include_router(sanitize.router)

@app.get("/health")
def health():
    return {"message":"I am healthy!"}
@app.get("/")
def index():
    return RedirectResponse(url="/home/index.html")
app.mount("/home",StaticFiles(directory="frontend"))