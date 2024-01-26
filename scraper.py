from os import getenv
from dotenv import load_dotenv
from lyricsgenius import Genius
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

genius = Genius(getenv("GENIUS_ACCESS_TOKEN"), remove_section_headers = True)
client = MongoClient(getenv("CONNECTION_STRING"), server_api = ServerApi('1'))
db = client.dev

artists = ["Andy Shauf", "Alan Walker", "Marshmello", "Daler Mehndi", "Arijit Singh"]

for artist in artists:
    try:
        songs = (genius.search_artist(artist, max_songs = 10, sort = "popularity")).songs
        for song in songs:
            db.songs.insert_one({
                "title": song.title,
                "artist": song.artist,
                "lyrics": song.lyrics.partition("Lyrics")[-1],
                "url": song.url
            })
    except:
        print("Error")