from pathlib import Path

from fastapi import APIRouter, FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

api_router = APIRouter(prefix="/frontend-api")


@api_router.get("/hello")
async def hello():
    return {"message": "Привет из бекенда!"}


app = FastAPI()
app.include_router(api_router)

app.mount(
    "/assets",
    StaticFiles(directory=FRONTEND_DIR / "assets"),
    name="assets",
)


@app.get("/")
async def index():
    return FileResponse(FRONTEND_DIR / "index.html")


@app.get("/frontend-settings.json")
async def get_settings():
    return FileResponse(BASE_DIR / "frontend-settings.json")
