from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post('/upload')
async def file_upload(file: UploadFile = File(...)):
    
    # Read uploaded file directly
    content = await file.read()
    text = content.decode("utf-8")
    
    lines = text.split("\n")

    error = 0
    info = 0
    warning = 0
    count = 0

    for line in lines:
        count += 1
        if "ERROR" in line:
            error += 1
        if "INFO" in line:
            info += 1
        if "WARNING" in line:
            warning += 1

    return {
        "Total": count,
        "ERROR": error,
        "WARNING": warning,
        "INFO": info
    }