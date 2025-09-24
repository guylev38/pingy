"""
Consts for the Pingy backend.

Author: guylev38
Date: 23/09/2025
"""

# ----- Imports ----- #

from enum import Enum
from pathlib import Path

# ----- Enums ----- #

class DeviceStatus(Enum):
    OFFLINE = False
    ONLINE = True

# ----- Consts ------ #

# Loggers 
DEVICES_LOGGER_NAME = "devices"
SYSTEM_LOGGER_NAME = "system"

# Database
DATABASE_PATH = Path("backend/database/")

