from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers.lectures import router as lecture_router

app = FastAPI(title="Lecture API")

# Mount static root (optional)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Mount chapter materials folder explicitly
app.mount(
    "/chapter-materials",
    StaticFiles(directory="static/chapter-materials"),
    name="chapter-materials"
)

# Mount lectures JSON folder
app.mount(
    "/lectures",
    StaticFiles(directory="static/lectures"),
    name="lectures"
)

# Include your router
app.include_router(lecture_router)
