from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse, RedirectResponse
# from .db import SessionLocal

from .routers.lms import lms_views
from .routers.user import user_views
app = FastAPI(
    title="intellity.ru backend v1",
    description="Альтернативная документация [redocs](/redoc)",
    summary="Deadpool's favorite app. Nuff said.",
    version="0.0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "http://localhost:5174/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def docs():
    return RedirectResponse("/docs")

@app.get("/r")
def docs():
    return RedirectResponse("/redoc")


app.include_router(lms_views, prefix="/api/v1/lms", tags=["основной функционал lms"])
app.include_router(user_views, prefix="/api/v1/user", tags=["основной функционал для работы с пользователями"])