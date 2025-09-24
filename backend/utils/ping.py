"""
Ping utilities.

Author: guylev38
Date: 23/09/2025
"""

# ----- Imports ----- #

import asyncio
import time
from typing import Any, Union

from backend.utils.loggers import (device_logger, system_logger)

# ----- Classes ----- #


class PingFailedError(BaseException):
    pass

class NoResponseTime(BaseException):
    pass

# ----- Functions ----- #

def parse_stdout(text: str) -> Union[float | None]:
    if "time=" in text:
        ms = text.split("time=")[1].split()[0]
        return float(ms.replace("ms", "").replace("=", ""))
    
    raise NoResponseTime


async def ping_cmd(device_ip: str, timeout: int) -> Union[float | None]:
    """
    Ping a device via subprocess and parse it.

    :param device_ip: The device's IP address.
    :param timeout: The ping command timeout.

    :return: The response time if the ping was successful, None otherwise.
    """

    process = await asyncio.create_subprocess_exec("ping", device_ip, "-c 10", f"-W {timeout}", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    
    system_logger.info(f"Pinging {device_ip}...")
    device_logger.info(f"Pinging {device_ip}...")
    stdout, _ = await process.communicate()
    system_logger.info(f"Finished pinging {device_ip}!")
    device_logger.info(f"Finished pinging {device_ip}!")

    if process.returncode != 0:
        raise PingFailedError

    try: 
        response_time = parse_stdout(stdout.decode().lower())
    except NoResponseTime:
        device_logger.error(f"Response time not found in ping stdout!")
        system_logger.error(f"Response time not found in ping stdout!")
        response_time = None

    return response_time


async def ping_device(device_id: str, device_ip: str, timeout: int) -> dict[str, Any]:
    """
    Ping a device and return the following information:
        - Device IP
        - Status 
        - Last Checked
        - Ping MS

    :param device_id: The device's id.
    :param device_ip: The device's IP address.
    :param timeout: Timeout for the ping.
    """

    response_time = None

    try:
        response_time = await ping_cmd(device_ip, timeout)
    except PingFailedError:
        device_logger.warning(f"Ping request to {device_ip} failed! Device is down!")
        system_logger.warning(f"Ping request to {device_ip} failed! Device is down!")

    result = {
        f"{device_id}": {
            "ip": device_ip,
            "status": "online" if response_time else "offline",
            "last_checked": time.strftime("%D/%M/%Y - %H:%M:%S"),
            "ping_ms": round(response_time * 1000, 2) if response_time else None
        }
    }  

    return result

