"""
Errors related to the database.

Author: guylev38
Date: 26/09/2025
"""

# ----- Classes ----- #


class DatabaseManagerAlreadyInitialized(BaseException):
    pass


class DeviceAlreadyExistsError(BaseException):
    pass


class DeviceNotFoundError(BaseException):
    pass


class DeviceInsertNotAcknowledged(BaseException):
    pass


class DeviceDeleteNotAcknowledged(BaseException):
    pass