"""
This class defines a device.

Author: guylev38
Date: 24/09/2025
"""

# ----- Imports ----- #
from typing import Optional

from pydantic import BaseModel

from backend.consts import DeviceStatus

# ----- Classes ----- #

class Device(BaseModel):
    ip: str 
    status: DeviceStatus = DeviceStatus.OFFLINE
    last_checked: Optional[str] = None
    response_time: Optional[float] = None


