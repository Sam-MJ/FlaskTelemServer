from app import app
from flask import g

from pathlib import Path
import sqlite3


DATABASE = Path(
    r"D:\Documents\Programming_stuff\Python_projects\FlaskTelemServer\SausageDB.db"
)


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
    try:
        cur = db.cursor()
        cur.execute(
            "INSERT INTO transactions (session_id, hashed_ip, hashed_mac, files_created, files_scanned, session_start, session_end) VALUES (?,?,?,?,?,?,?)",
            (
                transaction.session_id,
                transaction.hashed_ip,
                transaction.hashed_mac,
                transaction.files_created,
                transaction.files_scanned,
                transaction.session_start,
                transaction.session_end,
            ),
        )
        db.commit()
    except:
        db.rollback()
        return "500 - Database Error"
