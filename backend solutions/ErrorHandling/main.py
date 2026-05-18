import logging

import schemas
from models import base, Logging
from database import engine, SessionLocal
import auth

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session


# -------------------------
# Logging configuration
# -------------------------
logging.basicConfig(level=logging.INFO)

# Create tables
base.metadata.create_all(bind=engine)

app = FastAPI()


# -------------------------
# Database Dependency
# -------------------------
def getDb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------------------------
# Add Logs API
# -------------------------
@app.post(
    '/add-logs',
    dependencies=[Depends(auth.Auth)]
)
def add_logs(
    log: schemas.Logger,
    db: Session = Depends(getDb)
):

    logging.info("Add logs API called")

    try:
        # Create log object
        data = Logging(
            type=log.type,
            message=log.message
        )

        # Save to DB
        db.add(data)
        db.commit()
        db.refresh(data)

        logging.info(
            f"Log added successfully. ID: {data.id}"
        )

        return {
            "message": "Logs added successfully",
            "data": {
                "id": data.id,
                "level": data.type,
                "message": data.message
            }
        }

    except Exception as e:

        logging.error(
            f"Failed to add log: {str(e)}"
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to add log"
        )
@app.get('/get-logs')
def get_logs(
    id: int,
    db: Session = Depends(getDb)
):

    logging.info(
        f"get-logs API called for ID: {id}"
    )

    try:

        data = db.query(Logging).filter(
            Logging.id == id
        ).first()

        # If ID not found
        if data is None:

            logging.error(
                f"Log ID {id} not found"
            )

            raise HTTPException(
                status_code=404,
                detail="Log not found"
            )

        logging.info(
            f"Log ID {id} fetched successfully"
        )

        return data

    except HTTPException:
        raise

    except Exception as e:

        logging.error(
            f"Error occurred: {str(e)}"
        )

        raise HTTPException(
            status_code=500,
            detail="Something went wrong"
        )
        

