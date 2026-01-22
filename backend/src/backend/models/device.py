"""
This class defines a device.

Author: guylev38
Date: 24/09/2025
"""

# ----- Imports ----- #

import enum
import hashlib

from pydantic import BaseModel, Field, ConfigDict, model_validator 
from bson.objectid import ObjectId

# ----- Functions ----- #

def hash_ip(ip: str) -> ObjectId:
    ip_hash = hashlib.md5(ip.encode()).hexdigest()[:24]
    return ObjectId(ip_hash)


# ----- Classes ----- #


class DeviceStatus(enum.Enum):
    OFFLINE = False
    ONLINE = True


class Device(BaseModel):
    ip: str 
    status: bool | None = DeviceStatus.OFFLINE.value
    last_checked: str | None = None
    response_time: float | None = None
    id: ObjectId | None = Field(default=None, alias="_id")

    @model_validator(mode="before")
    @classmethod
    def compute_id(cls, values):
        if not values.get("id"):
            ip = values.get("ip")
            if ip:
                values["id"] = hash_ip(ip)
        return values


    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        json_encoders={ObjectId: str}
    )

