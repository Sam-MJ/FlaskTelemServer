from app.model import Transaction
from uuid import uuid4
import datetime
from pydantic import IPvAnyAddress, UUID4
import json
import requests


def test_send_transaction():

    telem_version: int = 1
    ip_address: IPvAnyAddress = "127.0.0.1"
    mac_address: str = "0xe0d55ef93bc0"
    session_id: UUID4 = uuid4()
    files_created: int = 300
    files_scanned: int = 6000
    session_start: datetime = datetime.datetime.now().isoformat()
    session_end: datetime = datetime.datetime.now().isoformat()

    t = Transaction(
        telem_version=telem_version,
        ip_address=ip_address,
        mac_address=mac_address,
        session_id=session_id,
        files_created=files_created,
        files_scanned=files_scanned,
        session_start=session_start,
        session_end=session_end,
    )

    payload = {
        "session_id": session_id,
        "files_created": files_created,
        "files_scanned": files_scanned,
        "session_start": session_start,
        "session_end": session_end,
    }

    payload_json = json.dumps(payload)

    r = requests.post(
        "http://127.0.0.1:5000/SausageFileConverterTransactions",
        json=payload_json,
    )
