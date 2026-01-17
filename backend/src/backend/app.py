"""
Pingy - Basic dashboard for networked devices.

Author: guylev38
Date: 23/09/2025
"""

# ----- Imports ----- #

import asyncio

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from backend.utils.loggers import system_logger
from backend.utils.ping import ping_device
from backend.database import DBManager
from backend.models import Device
from backend.errors.database_errors import DeviceAlreadyExistsError, DeviceNotFoundError

# ----- Globals ----- #

app = FastAPI()
db = DBManager()


# ----- Consts ----- #

TIMEOUT = 1
ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

CODE_OK = 200
CODE_NOT_FOUND = 404
CODE_CONFLICT = 409


# ----- Config ----- #

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# ----- Functions ----- #


@app.get("/api")
async def root():
    return {"message": "Welcome to Pingy!"}


@app.get("/api/status", response_class=JSONResponse)
async def status(response: JSONResponse) -> list[Device]:
    devices = await db.get_devices()
    ping_tasks = [ping_device(device.ip, TIMEOUT) for device in devices] 

    ping_results = await asyncio.gather(*ping_tasks)        

    try:
        await db.update_devices(ping_results)
    except DeviceNotFoundError:
        response = JSONResponse(content={"message": "DeviceNotFoundError"}, status_code=CODE_NOT_FOUND)
        return []

    response.status_code = CODE_OK
    return ping_results


@app.get("/api/devices")
async def devices() -> list[Device]:
    return await db.get_devices()

@app.post("/api/add_device", response_class=JSONResponse)
async def add_device(request: Request, device: Device):
    system_logger.info(f"Got {request.body}")
    try: 
        await db.add_devices([device])
        return JSONResponse(content={"message": "Device Added Successfully"}, status_code=CODE_OK)
    except DeviceAlreadyExistsError:
        return JSONResponse(content={"message": "DeviceAlreadyExistsError"}, status_code=CODE_CONFLICT)


@app.post("/api/delete_device", response_class=JSONResponse)
async def delete_device(request: Request, device: Device):
    system_logger.info(f"Got {request.body}")
    try: 
        await db.delete_devices([device])
        return JSONResponse(content={"message": "Device Removed Successfully!"}, status_code=CODE_OK)
    except DeviceNotFoundError:
        return JSONResponse(content={"message": "DeviceNotFoundError"}, status_code=CODE_NOT_FOUND)
