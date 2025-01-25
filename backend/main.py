from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import yt_dlp as youtube_dl
from urllib.parse import quote

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Replace "*" with your frontend URL for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directory to save downloaded videos
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Serve the downloads folder as static files
app.mount("/downloads", StaticFiles(directory=DOWNLOAD_DIR), name="downloads")

@app.post("/download/")
async def download_video(url: str = Form(...)):
    if not url.startswith("http"):
        raise HTTPException(status_code=400, detail="Invalid URL format.")

    try:
        ydl_opts = {
            "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
            "format": "best",
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get("title", "video")
            video_extension = info_dict.get("ext", "mp4")
            file_path = os.path.join(DOWNLOAD_DIR, f"{video_title}.{video_extension}")

        if os.path.exists(file_path):
            print(f"Downloaded: {file_path}")
            return JSONResponse(content={
                "success": True,
                "message": f"Downloaded {video_title}",
                "path": f"/downloads/{quote(video_title)}.{video_extension}"
            }, status_code=200)

        raise HTTPException(status_code=500, detail="Video download failed.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
