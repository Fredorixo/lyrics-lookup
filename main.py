from os import getenv
from torch import Tensor
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from fastapi import FastAPI, HTTPException, status
from sentence_transformers import SentenceTransformer, util

load_dotenv()

model = SentenceTransformer('all-MiniLM-L6-v2')
client = MongoClient(getenv("CONNECTION_STRING"))
collection = client["dev"]["songs"]
lyrics_embeddings = Tensor([document["embedding"] for document in collection.find()])

app = FastAPI(
    title = "Lyrics Lookup",
    description = "An API To Query Songs Related To Given Lyrics",
    docs_url = "/"
)

@app.get("/get-songs")
def get_songs(lyrics: str):
    try:
        query_embedding = model.encode(sentences = lyrics, convert_to_tensor = True)

        results = util.semantic_search(
            query_embeddings = query_embedding,
            corpus_embeddings = lyrics_embeddings,
            top_k = 10
        )[0]

        indexes = [result["corpus_id"] for result in results]
        outcome = [document for document in collection.find({"_id": {"$in": indexes}}, {"embedding": 0})]

        return {"songs": outcome}
    except:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "An Internal Server Error Occurred"
        )