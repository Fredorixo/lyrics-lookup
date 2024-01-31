from os import getenv
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from fastapi import FastAPI, HTTPException, status
from sentence_transformers import SentenceTransformer, util

load_dotenv()

model = SentenceTransformer('all-MiniLM-L6-v2')
client = MongoClient(getenv("CONNECTION_STRING"))
collection = client["dev"]["songs"]

app = FastAPI()

@app.get("/get-songs")
def get_songs(lyrics: str):
    try:
        lyrics_embeddings = [document["embeddings"] for document in collection.find()]
        query_embedding = model.encode(sentences = lyrics, convert_to_tensor = True)

        results = util.semantic_search(
            query_embeddings = query_embedding,
            corpus_embeddings = lyrics_embeddings,
            top_k = 10
        )[0]

        return {"Results": [result["corpus_id"] for result in results]}
    except:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)