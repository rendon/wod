from fastapi import FastAPI, HTTPException
import json

from wodparser import get_wod

app = FastAPI()

db = None
def get_words():
    global db
    if db is None:
        db = json.loads(open('db.json').read())
    return db

@app.get("/wod/")
def wod():
    return get_words()


# TODO: sanitize {date}
@app.get("/wod/{date}")
def wod_on_date(date: str):
    words = get_words()
    if date not in words:
        wod = get_wod(date)
        if wod:
            words[date] = wod

    if date in words:
        return {'date': date, 'word': words[date]}

    raise HTTPException(status_code=404, detail="Word not found")
