"""
Runner for the pingy backend.

:author: guylev38
:date: 09/01/2026
"""

# ----- Imports ----- #

import uvicorn
from backend.utils.loggers import (system_logger, device_logger)

# ----- Functions ----- #


def main():
    uvicorn.run("backend.app:app", host="127.0.0.1", port=8000, reload=True)
    system_logger.info("System Logger Ready") 
    device_logger.info("Device Logger Ready") 


# ----- Main Entry Point ----- #

if __name__ == "__main__":
    main()