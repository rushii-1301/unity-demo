from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers.lectures import router as lecture_router

app = FastAPI(title="Lecture API", docs_url="/docs", redoc_url="/redoc")

# Include your router FIRST (before static mounts to prevent conflicts)
app.include_router(lecture_router)

# Mount static files AFTER router (order matters!)
# Mount static root
app.mount("/static", StaticFiles(directory="static"), name="static")

# Mount chapter materials folder explicitly
app.mount(
    "/chapter-materials",
    StaticFiles(directory="static/chapter-materials"),
    name="chapter-materials"
)

# Mount lectures JSON folder
app.mount(
    "/lectures-static",
    StaticFiles(directory="static/lectures"),
    name="lectures-static"
)
