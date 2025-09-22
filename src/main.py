"""
Pingy - a little ping dashboard for networked devices.

Author: guylev38
Date: 20/09/2025
"""

# ----- Imports ----- # 

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# ----- Globals ----- #

app = FastAPI()
templates = Jinja2Templates(directory=""
                                      "assets/templates")

# ----- Config ----- #

app.mount("/assets/static", StaticFiles(directory="assets/static"), name="static")

# ----- Functions ----- # 


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    context = {"request": request, "message": "Hello!"}
    return templates.TemplateResponse("index.html", context)

