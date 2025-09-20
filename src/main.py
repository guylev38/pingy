"""
Pingy - a little ping dashboard for networked devices.

Author: guylev38
Date: 20/09/2025
"""

# ----- Imports ----- # 

from fastapi import FastAPI

# ----- Globals ----- #

app = FastAPI()

# ----- Functions ----- # 


@app.get("/")
async def root():
    return {"message": "Hello World"}


