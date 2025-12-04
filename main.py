from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers.lectures import router as lecture_router

app = FastAPI(title="Lecture API")

# Mount static folder for JSON + audio
app.mount("/static", StaticFiles(directory="static"), name="static")

# Register lecture routes
app.include_router(lecture_router)
