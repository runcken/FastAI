from pathlib import Path

from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

api_router = APIRouter(prefix="/frontend-api")


@api_router.get("/hello")
async def hello():
    return {"message": "Привет из бекенда!"}


user_data = {
    "email": "example@example.com",
    "isActive": True,
    "profileId": "1",
    "registeredAt": "2025-06-15T18:29:56+00:00",
    "updatedAt": "2025-06-15T18:29:56+00:00",
    "username": "user123",
}


class UserPublicProfile(BaseModel):
    email: str
    profileId: str
    username: str
    isActive: bool = True
    registeredAt: str
    updatedAt: str


@api_router.get("/users/me")
async def users_me(request: Request):
    return UserPublicProfile(**user_data)


app = FastAPI(title="FastAI", version="0.1.1")
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
