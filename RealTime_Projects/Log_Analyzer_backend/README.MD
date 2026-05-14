# Log Analyzer Backend API

A production-style backend application built using FastAPI to upload, parse, analyze, and filter log files.

This project demonstrates real-world backend concepts such as modular architecture, file upload handling, database integration, filtering, pagination, statistics generation, and API development.

---

## Features

✅ Upload `.log` files

✅ Parse log entries automatically

✅ Store logs in SQLite database

✅ Fetch all logs

✅ Filter logs by level (`INFO`, `WARNING`, `ERROR`)

✅ Search logs using keywords

✅ Filter logs by date

✅ Pagination support

✅ Log statistics API

✅ Error handling

✅ Swagger API documentation

✅ Modular project structure

---

## Project Structure

```text
log-analyzer-backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   └── logs.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── log_service.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── parser.py
│
├── logs/
│   └── sample.log
│
├── database/
│   └── logs.db
│
├── tests/
│   └── test_logs.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Tech Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Uvicorn
- Pytest

---

## Log File Format

Expected log format:

```text
2026-05-14 10:20:30 INFO User logged in
2026-05-14 10:22:15 ERROR Database connection failed
2026-05-14 10:25:00 WARNING High memory usage
```

---

## Installation

### Clone the repository

```bash
git clone <your-github-repo-url>
```

### Move into project folder

```bash
cd log-analyzer-backend
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

Start FastAPI server:

```bash
uvicorn app.main:app --reload
```

Application runs on:

```text
http://127.0.0.1:8000
```

Swagger API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Upload Log File

**POST**

```http
/logs/upload
```

Upload a `.log` file.

---

### Get All Logs

**GET**

```http
/logs
```

---

### Filter Logs by Level

**GET**

```http
/logs?level=ERROR
```

Examples:

```http
/logs?level=INFO
/logs?level=WARNING
/logs?level=ERROR
```

---

### Search Logs by Keyword

**GET**

```http
/logs?keyword=login
```

Example:

Returns logs containing the word:

```text
login
```

---

### Filter Logs by Date

**GET**

```http
/logs?date=2026-05-14
```

---

### Pagination

**GET**

```http
/logs?page=1&limit=10
```

Example:

```http
/logs?page=2&limit=5
```

---

### Get Log Statistics

**GET**

```http
/logs/stats
```

Sample Response:

```json
{
  "total_logs": 100,
  "info_count": 60,
  "warning_count": 25,
  "error_count": 15
}
```

---

## Example Workflow

1. Upload a log file

2. Logs are parsed automatically

3. Data is stored in SQLite database

4. Fetch logs using filters/search

5. Analyze statistics using API

---

## Future Improvements

- JWT Authentication
- PostgreSQL integration
- Docker support
- Cloud deployment
- Log visualization dashboard
- CSV export
- Rate limiting

---

## Learning Outcomes

This project demonstrates:

- REST API development
- FastAPI architecture
- Database integration
- File upload handling
- Pagination
- Query filtering
- Clean code structure
- Service-based architecture
- Error handling
- Backend project organization

---

## Author

**Sandhiya S**

Backend Developer | FastAPI | Python | OpenText ECM