"""
Runner for the pingy backend.

:author: guylev38
:date: 09/01/2026
"""

# ----- Imports ----- #

import uvicorn

# ----- Functions ----- #


def main():
    uvicorn.run("backend.app:app", host="127.0.0.1", port=8000, reload=True)


# ----- Main Entry Point ----- #

if __name__ == "__main__":
    main()