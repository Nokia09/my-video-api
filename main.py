import os
import requests
import random
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Danh sách các nguồn API video gái xinh ngẫu nhiên (Public)
# Mình tổng hợp một vài nguồn phổ biến, nếu nguồn này lỗi code sẽ tự chuyển nguồn khác
VIDEO_SOURCES = [
    "https://api.vungtau.xyz/video/gai",
    "https://api.vungtau.xyz/video/gaixinh",
    "https://api.vungtau.xyz/video/nude" # Tùy chọn nguồn bạn muốn
]

@app.get("/")
def home():
    return {"status": "success", "message": "API Video Online"}

@app.get("/api/get-video")
def get_video():
    # Chọn ngẫu nhiên một nguồn từ danh sách trên
    source = random.choice(VIDEO_SOURCES)
    try:
        # Gọi đến API nguồn để lấy link mp4
        response = requests.get(source, timeout=10)
        data = response.json()
        
        # Trả về link video cho bạn
        return {
            "status": "success",
            "video_url": data.get("url") or data.get("link"),
            "source_used": source
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    # Chạy trên Render hoặc WispByte đều được
    port = int(os.environ.get("SERVER_PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
