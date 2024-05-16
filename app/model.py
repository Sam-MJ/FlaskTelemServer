from pydantic import (
    BaseModel,
    UUID4,
    IPvAnyAddress,
    StringConstraints,
    field_validator,
    ValidationError,
)
from typing import Annotated
import datetime


class Transaction(BaseModel):

    telem_version: int
    ip_address: IPvAnyAddress
    mac_address: Annotated[str, StringConstraints(max_length=14, min_length=14)]
    session_id: UUID4 | Annotated[str, UUID4]
    files_created: int
    files_scanned: int
    session_start: datetime.datetime
    session_end: datetime.datetime

    @field_validator("mac_address")
    @classmethod
    def hex_str(cls, word):
        """Check string is a hex"""
        if not word.startswith("0x"):
            raise ValidationError("The game word must only contain letters")
        return word
