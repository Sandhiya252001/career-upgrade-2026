from fastapi import FastAPI, UploadFile, File
import os
from datetime import datetime

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post('/upload')
async def upload_logs(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save file to disk
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # Process file
    text = content.decode("utf-8")
    lines = text.splitlines()

    err = inf = warn = 0

    for i in lines:
        if "ERROR" in i:
            err += 1
        if "INFO" in i:
            inf += 1
        if "WARNING" in i:
            warn += 1

    return {
        "filename": file.filename,
        "path": file_path,
        "ERROR": err,
        "INFO": inf,
        "WARNING": warn,
        "Total": len(lines)
    }
@app.get('/filter')
async def filter_logs(filename: str, level: str, start: str, end: str):
    result = []

    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        return {"error": "File not found"}

    # Convert input time (HH:MM) → datetime.time
    start_time = datetime.strptime(start, "%H:%M").time()
    end_time = datetime.strptime(end, "%H:%M").time()

    with open(file_path, 'r') as f:
        for line in f:
            try:
                # Extract timestamp (first 19 chars)
                log_time = datetime.strptime(line[:19], "%Y-%m-%d %H:%M:%S").time()

                if (
                    level.upper() in line.upper()
                    and start_time <= log_time <= end_time
                ):
                    result.append(line.strip())

            except Exception:
                # Skip malformed lines
                continue

    return {"Result": result}