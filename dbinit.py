import sqlite3

conn = sqlite3.connect("SausageFileConverter-transactionsDB.db")

conn.execute(
    "CREATE TABLE transactions (telem_version INTEGER, ip_address TEXT, mac_address TEXT, session_id TEXT, files_created INTEGER, files_scanned INTEGER, session_start TEXT, session_end TEXT)"
)

conn.close
