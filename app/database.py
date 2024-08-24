import os
from app import app
from flask import g

import sqlite3
from sqlite3 import DatabaseError


DATABASE = os.environ["DATABASE_PATH"]


def get_db():
    """get database from global application context, if it doesn't exist create a new connection and return it."""
    db = getattr(g, "_database", None)

    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        print("open db")
    return db


@app.teardown_appcontext
def close_connection(exception):
    """once a request has finished, if a database has been opened, close it."""
    db = getattr(g, "_database", None)

    if db is not None:
        db.close()
        print("close db")


def db_write(transaction):
    """Write to db.
    If there is an existing entry for this session, update it
    If not, create an entry
    """
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
