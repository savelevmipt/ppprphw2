from fastapi import FastAPI
import time
import requests
app = FastAPI()

CALLS = 0

@app.get("/time")
def read_time():
    global CALLS
    CALLS += 1
    return requests.get('https://worldtimeapi.org/api/timezone/Europe/Moscow').json().get("datetime")

@app.get("/statistics")
def get_statistics():
    return CALLS

