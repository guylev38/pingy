"""
Pingy - Basic dashboard for networked devices.

Author: guylev38
Date: 23/09/2025
"""

# ----- Imports ----- #

import asyncio
import logging
from typing import Any

import uvicorn
from fastapi import FastAPI

from backend.utils.ping import ping_device
from backend.utils.loggers import (device_logger, system_logger)


# ----- Globals ----- #

app = FastAPI()

# ----- Consts ----- #

DEVICES = [
    {"ip": "192.168.0.100"},
    {"ip": "192.168.0.8"},
    {"ip": "192.168.0.11"}
]

TIMEOUT = 1

# ----- Functions ----- #


@app.get("/")
async def root():
    return {"message": "Welcome to Pingy!"}


@app.get("/status")
async def status() -> list[dict[str, Any]]:
    ping_tasks = [ping_device(device["ip"], TIMEOUT) for device in DEVICES]
    results = await asyncio.gather(*ping_tasks)
    
    return results

