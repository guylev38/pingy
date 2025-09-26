"""
Errors related to the ping module.

Author: guylev38 
Date: 26/09/2025
"""

# ----- Classes ----- #


class PingFailedError(BaseException):
    pass

class NoResponseTime(BaseException):
    pass
