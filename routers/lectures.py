from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pathlib import Path
import json

from config import LECTURE_PLAY_DATA

router = APIRouter()

# ---------------------------------------------------------
# 1️⃣ Route: /lectures/{lecture_id}/play
# ---------------------------------------------------------

@router.get("/lectures/{lecture_id}/play")
def get_lecture_play(lecture_id: str):
    """
    Returns metadata containing the lecture_url.
    """
    data = LECTURE_PLAY_DATA.get(lecture_id)

    if not data:
        return JSONResponse(
            status_code=404,
            content={"error": "Lecture not found"}
        )

    return data


# ---------------------------------------------------------
# 2️⃣ Route: /lectures/{grade}/{subject}/{lecture_id}.json
# Loads real JSON file
# ---------------------------------------------------------

@router.get("/lectures/{grade}/{subject}/{lecture_id}.json")
def get_lecture_json(grade: str, subject: str, lecture_id: str):
    """
    Loads actual lecture JSON from /static folder.
    """
    file_path = Path(f"static/lectures/{grade}/{subject}/{lecture_id}.json")

    if not file_path.exists():
        return JSONResponse(
            status_code=404,
            content={"error": "Lecture JSON file not found"}
        )

    with open(file_path, "r", encoding="utf-8") as f:
        lecture_data = json.load(f)

    return lecture_data


# ---------------------------------------------------------
# 3️⃣ Route: Serve Audio Files Automatically
# Example: /chapter-materials/chapter_lecture/audio/22/slide-1.mp3
# ---------------------------------------------------------

@router.get("/chapter-materials/chapter_lecture/audio/{lecture_id}/{filename}")
def get_audio_file(lecture_id: str, filename: str):
    """
    Serves MP3 or any audio files from static directory.
    """

    audio_path = Path(f"static/chapter-materials/chapter_lecture/audio/{lecture_id}/{filename}")

    if not audio_path.exists():
        return JSONResponse(
            status_code=404,
            content={"error": "Audio file not found"}
        )

    # FastAPI automatically serves file as FileResponse
    from fastapi.responses import FileResponse
    return FileResponse(audio_path)
