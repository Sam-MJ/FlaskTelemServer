from pydantic import BaseModel, UUID4, StringConstraints
from typing import Annotated
import datetime


class Transaction(BaseModel):

    telem_version: int
    product_id: int
    session_id: UUID4 | Annotated[str, UUID4]
    """ hashed_ip: Annotated[str, StringConstraints(max_length=60, min_length=60)]
    hashed_mac: Annotated[str, StringConstraints(max_length=60, min_length=60)] """
    files_created: int
    files_scanned: int
    session_start: datetime.datetime
    session_end: datetime.datetime
