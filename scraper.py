from os import getenv
from dotenv import load_dotenv
from lyricsgenius import Genius
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from sentence_transformers import SentenceTransformer

load_dotenv()

model = SentenceTransformer('all-MiniLM-L6-v2')
genius = Genius(access_token = getenv("GENIUS_ACCESS_TOKEN"), remove_section_headers = True)
client = MongoClient(host = getenv("CONNECTION_STRING"), server_api = ServerApi('1'))
db = client["dev"]["songs"]

artists = [item["item"]["name"] for item in (genius.charts(
    type_ = "artists",
    time_period = "all_time",
    per_page = 50
))["chart_items"]]

for artist in artists:
    try:
        songs = (genius.search_artist(
            artist_name = artist,
            max_songs = 20,
            sort = "popularity"
        )).songs
        
        for song in songs:
            song_lyrics = " ".join(song.lyrics.partition("Lyrics")[-1].split())

            db.insert_one({
                "title": song.title,
                "artist": song.artist,
                "lyrics": model.encode(sentences = song_lyrics),
                "url": song.url,
                "position": db.count_documents + 1
            })
    except:
        print("Error")