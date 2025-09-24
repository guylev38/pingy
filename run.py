"""
Entry script for Pingy.

Author: guylev38
Date: 23/09/2025
"""

# ----- Imports ----- #

import logging

import uvicorn

from backend.main import app
from backend.utils.loggers import (device_logger, system_logger)

# ----- Entry Point ----- #

if __name__ == "__main__":
    device_logger.info("Device logger ready!")
    system_logger.info("System logger ready!")

    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
