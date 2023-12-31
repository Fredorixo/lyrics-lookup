import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

client = MongoClient(os.getenv("CONNECTION_STRING"), server_api = ServerApi('1'))
db = client.dev

try:
    demand = input("Enter Lyrics: ")
    songs = db.songs.find({"$text": {"$search": demand}}).limit(10)
    for song in songs:
        print(f"\nTitle: {song["title"]}")
        print(f"Artist: {song["artist"]}")
        print("Lyrics:")

        for counter, line in enumerate([line for line in song["lyrics"].split("\n") if line != ""]):
            if counter == 4:
                break
            print(line)
        
        print(f"URL: {song["url"]}")
except Exception as e:
    print(e)