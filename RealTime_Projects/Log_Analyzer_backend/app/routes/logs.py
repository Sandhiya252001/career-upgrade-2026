from fastapi import APIRouter, UploadFile, File
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.log_service import (
    save_logs_from_file,
    get_logs_service,
    get_stats_service
)

router = APIRouter(
    prefix="/logs",
    tags=["Logs"]
)


@router.post("/upload")
async def upload_log_file(
        file: UploadFile = File(...),
        db: Session = Depends(get_db)
):

    if not file.filename.endswith(".log"):
        raise HTTPException(
            status_code=400,
            detail="Only .log files are allowed"
        )

    content = await file.read()

    return save_logs_from_file(
        content,
        db
    )


@router.get("/")
def get_logs(
        level: str = None,
        keyword: str = None,
        date: str = None,
        page: int = 1,
        limit: int = 10,
        db: Session = Depends(get_db)
):

    logs = get_logs_service(
        db=db,
        level=level,
        keyword=keyword,
        date=date,
        page=page,
        limit=limit
    )

    if not logs:
        raise HTTPException(
            status_code=404,
            detail="No logs found"
        )

    return logs


@router.get("/stats")
def get_stats(
        db: Session = Depends(get_db)
):

    return get_stats_service(db)