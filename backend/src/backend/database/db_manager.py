"""
JSON Database for the devices.

Author: guylev38
Date: 24/09/2025
"""

# ----- Imports ----- #

from pymongo.asynchronous.mongo_client import AsyncMongoClient 
from pymongo.errors import DuplicateKeyError

from backend.utils.loggers import system_logger
from backend.database import AbstractDatabaseManager
from backend.models import Device
from backend.errors.database_errors import (DatabaseManagerAlreadyInitialized, 
                                            DeviceAlreadyExistsError, 
                                            DeviceNotFoundError,
                                            DeviceInsertNotAcknowledged,
                                            DeviceDeleteNotAcknowledged)


# ----- Consts ----- #

MONGODB_ADDRESS = "mongodb://localhost:27017/"
DATABASE_NAME = "PingyDB"
COLLECTION_NAME = "Devices"

# ----- Classes ----- #


class DBManager(AbstractDatabaseManager):

    _is_initiazlied: bool = False 

    def __init__(self):
        if self._is_initiazlied:
            raise DatabaseManagerAlreadyInitialized

        self._mongo_client = AsyncMongoClient(MONGODB_ADDRESS)
        self._database = self._mongo_client[DATABASE_NAME]
        self._collection = self._database[COLLECTION_NAME]


    async def add_devices(self, devices: list[Device]): 
        for device in devices:
            try:
                system_logger.info(f"Inserting device {device.ip} to the database...")
                insert_result = await self._collection.insert_one(device.model_dump(by_alias=True)) 
            except DuplicateKeyError:
                system_logger.error(f"Device already exists!")
                raise DeviceAlreadyExistsError

            if not insert_result.acknowledged:
                system_logger.error(f"Database server didn't acknowledge insert request of device {device.ip}!")
                raise DeviceInsertNotAcknowledged
            
            system_logger.info(f"Device {device.ip} added successfully!")


    async def delete_devices(self, devices: list[Device]): 
        for device in devices:
            delete_result = await self._collection.delete_one(device.model_dump(by_alias=True))

            if delete_result.deleted_count == 0:
                system_logger.error(f"Device {device.ip} not found in database!")
                raise DeviceNotFoundError

            if not delete_result.acknowledged:
                system_logger.error(f"Database server didn't acknowledge request of device {device.ip}")
                raise DeviceDeleteNotAcknowledged

            system_logger.info(f"Device {device.ip} deleted successfully!")


    async def update_devices(self, devices: list[Device]): 
        for device in devices: 
            device_filter = {"_id": device.id}
            system_logger.info(f"Updating device {device.ip} database entry...")
            update_result = await self._collection.replace_one(device_filter, device.model_dump(by_alias=True))

            if update_result.modified_count == 0:
                system_logger.error(f"Device {device.ip} not found in database!")
                raise DeviceNotFoundError
            
            system_logger.info(f"Device {device.ip} database entry updated successfully!")


    async def get_devices(self, devices: list[Device] | None = None) -> list[Device]:  
        queried_devices: list[Device] = []

        if devices is None:
            async for device in self._collection.find():
                queried_devices.append(Device(**device))
            return queried_devices

        for device in devices:
            find_result = self._collection.find_one({"_id": device.id})
            if find_result is None:
                system_logger.error(f"Device {device.ip} not found in database") 
                raise DeviceNotFoundError

            queried_devices.append(Device.model_validate(find_result))

        return queried_devices