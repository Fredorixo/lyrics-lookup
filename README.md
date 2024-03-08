# Lyrics Lookup

![image](https://github.com/Fredorixo/lyrics-lookup/assets/80041092/c1a9ef85-d305-47ec-ae39-e18d4198ad83)

## Introduction

An API built using FastAPI, a modern web framework, to recommend top 10 relevant songs in accordance with user's prompted lyrics.

## API Reference

#### Get 10 songs relevant to your prompted lyrics

```bash
  GET /get-songs?lyrics=${your_lyrics}
```

| Parameter      | Type     | Description                     |
| :------------- | :------- | :------------------------------ |
| `your_lyrics`  | `string` | **Required**. Your query lyrics |


## Run Locally

To run the project locally,

1. Clone the project

```bash
git clone https://github.com/Fredorixo/lyrics-lookup.git
```

2. Go to the project directory

```bash
cd lyrics-lookup
```

3. Create a .env file according to .env.example file and place your MongoDB API key there

4. To create and enter into a virtual environment

```bash
pipenv shell --python <python_version>
```

5. To execute your local development server

```bash
uvicorn main:app --reload
```

## Learnings

- Used `pipenv` for creating a virtual environment to perform development in an isolated environment, having a different python version and maintaing packages locally.
- Employed `pyenv` for maintaing different python versions without hassle.
- Used FastAPI in conjunction with MongoDB to make the setup work.
- Made use of a MiniLM in sentence transformer to perform semantic search on the embedding space with the query lyrics in consideration.
- Learnt about cron jobs, to regularise a job at certain time intervals.
