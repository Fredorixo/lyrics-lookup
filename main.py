from os import getenv
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from fastapi import FastAPI, HTTPException, status
# from sentence_transformers import util
# from torch import topk

load_dotenv()

client = MongoClient(getenv("CONNECTION_STRING"), server_api = ServerApi('1'))
db = client.dev

app = FastAPI()

@app.get("/get-songs")
def get_songs(lyrics: str):
    try:
        songs = db.songs.find({"$text": {"$search": lyrics}}).limit(10)
        return songs
    except:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)