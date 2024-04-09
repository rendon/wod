from fastapi import FastAPI
import json

app = FastAPI()

db = None
def get_words():
    global db
    if db is None:
        db = json.loads(open('db.json').read())
    return db

@app.get("/wod/")
def read_root():
    return get_words()
