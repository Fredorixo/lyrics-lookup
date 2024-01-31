from os import getenv
from dotenv import load_dotenv
from lyricsgenius import Genius
from pymongo.mongo_client import MongoClient
from sentence_transformers import SentenceTransformer

load_dotenv()

model = SentenceTransformer('all-MiniLM-L6-v2')
genius = Genius(access_token = getenv("GENIUS_ACCESS_TOKEN"), remove_section_headers = True)
client = MongoClient(host = getenv("CONNECTION_STRING"))
collection = client["dev"]["songs"]

artists = []

for page in [1, 2]:
    for result in (genius.charts(type_ = "artists", per_page = 50, page = page))["chart_items"]:
        artist = result["item"]["name"]

        if artist.isascii() and "Genius" not in artist:
            artists.append(artist)

for artist in artists:
    try:
        songs = (genius.search_artist(
            artist_name = artist,
            max_songs = 30,
            sort = "popularity"
        )).songs
        
        for song in songs:
            if(collection.find({"title": song.title, "artist": song.artist})):
                continue

            song_lyrics = " ".join(song.lyrics.partition("Lyrics")[-1].split())

            collection.insert_one({
                "_id": collection.estimated_document_count() + 1,
                "title": song.title,
                "artist": song.artist,
                "embeddings": model.encode(sentences = song_lyrics, convert_to_tensor = True),
                "url": song.url
            })
    except:
        print("Error")