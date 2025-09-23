"""
Loggers for Pingy backend.

Author: guylev38
Date: 23/09/2025
"""

# ----- Imports ----- #

import logging

from backend.consts import DEVICES_LOGGER_NAME, SYSTEM_LOGGER_NAME

# ----- Consts ----- #

DEVICE_LOGGER_FORMAT = {
        "fmt": "[%(asctime)s] [%(levelname)s] %(message)s", 
        "datefmt": "%d/%m/%Y %H:%M:%S"
    }

SYSTEM_LOGGER_FORMAT = {
        "fmt": "[%(asctime)s] [%(levelname)s] [%(module)s:%(funcName)s] %(message)s", 
        "datefmt": "%d/%m/%Y %H:%M:%S",
    }

# ----- Functions ----- #


def create_device_logger() -> logging.Logger:
    """
    Configures the device logger, will be used to log the periodic ping results.
    Logs to a file and to the console. 

    :return: The device logger.
    """

    device_logger = logging.getLogger(DEVICES_LOGGER_NAME)
    device_logger.setLevel(level=logging.INFO)
    formatter = logging.Formatter(**DEVICE_LOGGER_FORMAT)

    # Console 
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)        
    console_handler.setFormatter(formatter)

    # File -> TODO: Remember to set a limit on the file so that it won't get really big.
    file_handler = logging.FileHandler("logs/devices.log", mode="a")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    device_logger.addHandler(console_handler)
    device_logger.addHandler(file_handler)

    return device_logger


def create_system_logger() -> logging.Logger:
    """
    Configures the system logger.
    Logs to the console.

    :return: The system logger.
    """
    
    system_logger = logging.getLogger(SYSTEM_LOGGER_NAME)
    system_logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(**SYSTEM_LOGGER_FORMAT)

    # Console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    system_logger.addHandler(console_handler)
    system_logger.propagate = True

    return system_logger


device_logger = create_device_logger()
system_logger = create_system_logger()

