from sqlalchemy.orm import Session
from app.models import Log
from app.utils.parser import parse_log_line


def save_logs_from_file(file_content, db: Session):

    lines = file_content.decode("utf-8").splitlines()

    saved_logs = []

    for line in lines:

        parsed = parse_log_line(line)

        if parsed:

            log = Log(
                timestamp=parsed["timestamp"],
                log_level=parsed["log_level"],
                message=parsed["message"]
            )

            db.add(log)
            saved_logs.append(log)

    db.commit()

    return {
        "message": f"{len(saved_logs)} logs uploaded successfully"
    }


def get_logs_service(
        db: Session,
        level=None,
        keyword=None,
        date=None,
        page=1,
        limit=10
):

    query = db.query(Log)

    if level:
        query = query.filter(
            Log.log_level.ilike(level)
        )

    if keyword:
        query = query.filter(
            Log.message.ilike(f"%{keyword}%")
        )

    if date:
        query = query.filter(
            Log.timestamp.contains(date)
        )

    skip = (page - 1) * limit

    logs = query.offset(skip).limit(limit).all()

    return logs


def get_stats_service(db: Session):

    total_logs = db.query(Log).count()

    info_count = db.query(Log).filter(
        Log.log_level == "INFO"
    ).count()

    warning_count = db.query(Log).filter(
        Log.log_level == "WARNING"
    ).count()

    error_count = db.query(Log).filter(
        Log.log_level == "ERROR"
    ).count()

    return {
        "total_logs": total_logs,
        "info_count": info_count,
        "warning_count": warning_count,
        "error_count": error_count
    }