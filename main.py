from fastapi import FastAPI
from typing import Union
from mangum import Mangum

app=FastAPI()

@app.get("/")
async def root():
    return {'message':'Hello AWS'}