"""
Pingy - Basic dashboard for networked devices.

Author: guylev38
Date: 23/09/2025
"""

# ----- Imports ----- #

import asyncio
from typing import Any

from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse

from backend.utils.ping import ping_device
from backend.utils.loggers import (device_logger, system_logger)
from backend.database import MongoManager
from backend.errors import (DeviceAlreadyExistsError, DeviceNotFoundError)
from backend.models import Device


# ----- Globals ----- #

app = FastAPI()
db = MongoManager("db.json")

# ----- Consts ----- #

TIMEOUT = 1

# ----- Functions ----- #


@app.get("/")
async def root():
    return {"message": "Welcome to Pingy!"}


@app.get("/status")
async def status() -> dict[str, Device]:
    ping_tasks = [ping_device(device_id, device["ip"], TIMEOUT) for device_id, device in db.get_devices().items()]
    raw_results = await asyncio.gather(*ping_tasks)
    results = {}

    for raw_result in raw_results:
       device_id, device = next(iter(raw_result.items()))
       results[device_id] = device

    db.update(results)

    return results

@app.get("/devices")
async def devices() -> dict[str, Any]:
    return db.get_devices()


@app.post("/add_device", response_class=JSONResponse)
async def add_device(device: Device):
    try:
        db.add_device(device)
    except DeviceAlreadyExistsError:
        return JSONResponse(
            content={"message": f"Device {device.ip} already exists"},
            status_code=409 # Conflict
        )

@app.post("/remove_device", response_class=JSONResponse)
async def remove_device(ip: str = Form(...)):
    try:
        db.remove_device(ip)
    except DeviceNotFoundError:
        return JSONResponse(
            content={"message": f"Device {ip} doesn't exist"},
            status_code=404 # Not-Found
        )
    
    return JSONResponse(
        content={"message": f"Device {ip} removed successfully"},
        status_code=200 # OK
    )
        
