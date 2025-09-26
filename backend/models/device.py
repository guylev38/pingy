"""
This class defines a device.

Author: guylev38
Date: 24/09/2025
"""

# ----- Imports ----- #

import enum
import hashlib
from typing import Optional

from pydantic import BaseModel

from backend.consts import DeviceStatus

# ----- Classes ----- #


class DeviceStatus(enum.Enum):
    OFFLINE = False
    ONLINE = True


class Device(BaseModel):
    _id: str = None
    ip: str 
    status: DeviceStatus = DeviceStatus.OFFLINE
    last_checked: Optional[str] = None
    response_time: Optional[float] = None
    
    @classmethod
    def _hash_ip(cls) -> str:
        return hashlib.md5(cls.ip.encode()).hexdigest()
    

    @property
    def id(cls) -> str:
        return cls._id


    @classmethod
    def from_ip(cls, ip: str, **kwargs):
        """
        Factory function to build a device with a hashed _id from IP.
        """
        return cls(_id=cls._hash_ip(), ip=ip, **kwargs)
