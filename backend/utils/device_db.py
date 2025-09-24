"""
JSON Database for the devices.

Author: guylev38
Date: 24/09/2025
"""

# ----- Imports ----- #

import json
import hashlib
from typing import Any
from pathlib import Path

from backend.consts import DATABASE_PATH
from backend.models import Device

# ----- Classes ----- #

class DeviceAlreadyExistsError(BaseException):
    pass

class DeviceNotFoundError(BaseException):
    pass

class DeviceDatabase:
    """
    A database class to manage devices in a JSON file.
    """

    def __init__(self, path: Path):
        self._path = path
        with open(DATABASE_PATH / self._path, "r") as db:
            self._data = json.load(db)


    def _save(self):
        with open(DATABASE_PATH / self._path, "w") as db:
            json.dump(self._data, db, indent=4)
        
    @staticmethod
    def _hash_ip(ip: str):
        hashed_ip = hashlib.md5(ip.encode())
        return hashed_ip.hexdigest()

    
    def _is_device_registered(self, ip: str) -> bool:
        return self._hash_ip(ip) in self._data.keys()
    

    def add_device(self, device: Device):
        if self._is_device_registered(device.ip):
            raise DeviceAlreadyExistsError

        self._data[self._hash_ip(device.ip)] = device.model_dump()
        
        self._save()
        

    def remove_device(self, ip: str):
        if not self._is_device_registered(ip):
            raise DeviceNotFoundError

        del self._data[self._hash_ip(ip)]
        self._save()
    

    def get_device(self, ip: str) -> Device | None:
        device_data = self._data.get(self._hash_ip(ip)) 
        if device_data:
           return Device(**device_data)
        return None
    
    def get_devices(self) -> dict[str, Any]:
        return self._data

    def update(self, updated_data: dict[str, Device]):
        self._data = updated_data
        self._save()