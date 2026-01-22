"""
Abstract Database Manager for pingy.

Author: guylev38
Date: 26/09/2025
"""

# ----- Imports ----- #

import abc

from backend.models import Device

# ----- Classes ----- #


class AbstractDatabaseManager(abc.ABC):
    """
    Describes an abstract database manager. 
    """

    @abc.abstractmethod
    async def add_devices(self, devices: list[Device]): 
        """
        Insert devices into the database

        :param devices: A list of devices to insert.
        """
        pass
    

    @abc.abstractmethod
    async def delete_devices(self, devices: list[Device]): 
        """
        Remove devices from teh database.
        
        :param devices: A list of devices to remove.
        """
        pass


    @abc.abstractmethod
    async def update_devices(self, devices: list[Device]): 
        """
        Update devices in the database.

        :param devices: A list of updated devices.
        :note: The devices argument should be passed as a list where all elements are devices with updated information. 
        """
        pass   


    @abc.abstractmethod
    async def get_devices(self, devices: list[Device] | None = None) -> list[Device]: 
        """
        Get devices from the database.

        :param devices: A list of devices to get from the database, if None will return all the devices in the database.
        :return: A list of devices.
        """
        pass

    