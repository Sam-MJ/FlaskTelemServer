import os
from app import app
from flask import g

from pathlib import Path
import sqlite3
from sqlite3 import DatabaseError


DATABASE = os.environ["DATABASE_PATH"]


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        print("open db")
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()
        print("close db")


def db_write(transaction):
    db = get_db()
    print("write")
    try:
        cur = db.cursor()
        cur.execute(
            "UPDATE transactions SET files_created = ?, files_scanned = ?, session_end = ? WHERE session_id = ?;",
            (
                transaction.files_created,
                transaction.files_scanned,
                transaction.session_end,
                transaction.session_id,
            ),
        )

        if cur.rowcount == 0:
            cur.execute(
                "INSERT INTO transactions (telem_version, ip_address, mac_address, session_id, files_created, files_scanned, session_start, session_end) VALUES (?,?,?,?,?,?,?,?);",
                (
                    transaction.telem_version,
                    str(transaction.ip_address),
                    transaction.mac_address,
                    transaction.session_id,
                    transaction.files_created,
                    transaction.files_scanned,
                    transaction.session_start,
                    transaction.session_end,
                ),
            )
        db.commit()
    except DatabaseError:
        db.rollback()
        raise DatabaseError
