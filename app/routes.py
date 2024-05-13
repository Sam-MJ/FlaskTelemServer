from flask import request
from pydantic import ValidationError
from app.model import Transaction
import json
from app.database import db_write
from sqlite3 import DatabaseError

from app import app


@app.route("/")
def hello():
    return "<p>Hello, World!</p>"


@app.post("/SausageFileConverterTransactions")
def receive_transaction():
    content_type = request.headers.get("Content-Type")
    print(content_type)
    data = request.json
    data = json.loads(data)
    print(data["session_id"])

    # validate inputs with pydantic model
    try:
        t = Transaction(
            telem_version=data["telem_version"],
            product_id=data["product_id"],
            session_id=data["session_id"],
            files_created=data["files_created"],
            files_scanned=data["files_scanned"],
            session_start=data["session_start"],
            session_end=data["session_end"],
        )
    except ValidationError as e:
        return (
            f"400"  # - {e}"  # - DEBUG ONLY! in production don't give more information
        )

    try:
        db_write(t)
    except DatabaseError:
        return "500 - Internal Error"

    return "201 - Transaction Created"
