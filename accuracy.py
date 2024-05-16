from os import getenv
from statistics import median
from torch import Tensor
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from sentence_transformers import SentenceTransformer, util

load_dotenv()

model = SentenceTransformer('all-MiniLM-L6-v2')
client = MongoClient(getenv("CONNECTION_STRING"))
collection = client["dev"]["songs"]
lyrics_embeddings = Tensor([document["embedding"] for document in collection.find()])

data = [
    {"id": 1, "lyrics": "You know I've never really met someone like you."},
    {"id": 32, "lyrics": "It's gon' burn for me to say this, but it's comin' from my heart"},
    {"id": 46, "lyrics": "I'm your number one fan, give me your autograph"},
    {"id": 82, "lyrics": "You need to calm down, you're being too loud"},
    {"id": 86, "lyrics": "I didn't choose this town, I dream of getting out"},
    {"id": 107, "lyrics": "Don't fall on my face"},
    {"id": 123, "lyrics": "I can feel your halo, halo, halo"},
    {"id": 141, "lyrics": "What is your aspiration in life?"},
    {"id": 149, "lyrics": "Heaven couldn't wait for you"},
    {"id": 180, "lyrics": "I've seen the world, lit it up as my stage now"},
    {"id": 221, "lyrics": "Forgive my northern attitude, oh, I was raised out in the cold"},
    {"id": 282, "lyrics": "We riding Bronco's right through the hill"},
    {"id": 322, "lyrics": "Be each other's company"},
    {"id": 341, "lyrics": "This time around, bring your friend with you"},
    {"id": 380, "lyrics": "Nah, nah, please don't wake me up, feel like I'm dreamin'"},
    {"id": 427, "lyrics": "All-white Gucci suit, I'm feeling righteous, yeah"},
    {"id": 461, "lyrics": "Hear the chatter, but I'm never switchin"},
    {"id": 522, "lyrics": "Took him out to Belgium, welcome"},
    {"id": 562, "lyrics": "We don't fit in well 'cause we are just ourselves"},
    {"id": 681, "lyrics": "I know that it breaks your heart when I cry"},
]

sum = 0
ranks = []
zero_count = 0

for item in data:
    try:
        query_embedding = model.encode(sentences = item["lyrics"], convert_to_tensor = True)

        results = util.semantic_search(
            query_embeddings = query_embedding,
            corpus_embeddings = lyrics_embeddings,
            top_k = 10
        )[0]

        found = False
        rank = 1

        for result in results:
            if(result["corpus_id"] == item["id"]):
                sum = sum + 1 / rank
                ranks.append(rank)
                found = True
                break

            rank = rank + 1
        
        if(found == False):
            zero_count = zero_count + 1
    except:
        print("Error")

score = sum / len(data)

print(f"MRR: {score}")
print(f"Median: {median(ranks)}")
print(f"Zero Count: {zero_count}")