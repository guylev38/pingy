"""
Pingy - Basic dashboard for networked devices.

Author: guylev38
Date: 23/09/2025
"""

# ----- Imports ----- #

import asyncio
from typing import Any

from fastapi import FastAPI, Form, Response
from fastapi.responses import JSONResponse

from backend.utils.ping import ping_device
from backend.utils.loggers import (device_logger, system_logger)
from backend.database import DBManager
from backend.models import Device
from backend.errors.database_errors import DeviceAlreadyExistsError, DeviceNotFoundError


# ----- Globals ----- #

app = FastAPI()
db = DBManager()

# ----- Consts ----- #

TIMEOUT = 1

# ----- Functions ----- #


@app.get("/")
async def root():
    return {"message": "Welcome to Pingy!"}


@app.get("/status")
async def status(response: Response) -> list[Device]:
    devices = await db.get_devices()
    ping_tasks = [ping_device(device.ip, TIMEOUT) for device in devices] 

    ping_results = await asyncio.gather(*ping_tasks)        

    try:
        await db.update_devices(ping_results)
    except DeviceNotFoundError:
        response.status_code = 404
        response.body = {"message": "DeviceNotFoundError"}
        return []

    response.status_code = 200 
    return ping_results


@app.get("/devices")
async def devices() -> list[Device]:
    return await db.get_devices()


@app.post("/add_device", response_class=JSONResponse)
async def add_device(device: Device):
    try: 
        await db.add_devices([device])
        return JSONResponse(content={"message": "Device Added Successfully"}, status_code=200)
    except DeviceAlreadyExistsError:
        return JSONResponse(content={"message": "DeviceAlreadyExistsError"}, status_code=409)

@app.post("/delete_device", response_class=JSONResponse)
async def delete_device(device: Device):
    try: 
        await db.delete_devices([device])
        return JSONResponse(content={"message": "Device Removed Successfully!"}, status_code=200)
    except DeviceNotFoundError:
        return JSONResponse(content={"message": "DeviceNotFoundError"}, status_code=404)