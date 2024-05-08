from flask import request
from pydantic import ValidationError
from app.model import Transaction
import json
from app.database import db_write

from app import app


@app.route("/")
def hello():
    return "<p>Hello, World!</p>"


@app.post("/SausageFileConverterTransactions")
def save_transaction():
    content_type = request.headers.get("Content-Type")
    print(content_type)
    data = request.json
    data = json.loads(data)
    print(data["session_id"])

    # validate inputs
    try:
        t = Transaction(
            session_id=data["session_id"],
            files_created=data["files_created"],
            files_scanned=data["files_scanned"],
            session_start=data["session_start"],
            session_end=data["session_end"],
        )
    except ValidationError as e:
        print(e)
        return f"400 - {e}"  # - DEBUG ONLY! in production don't give more information

    db_write(t)

    return "201 - Transaction Created"
