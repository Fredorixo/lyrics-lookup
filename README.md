# Lyrics Lookup

<br />
<div align="center">  
  <img src="https://github.com/Fredorixo/lyrics-lookup/assets/80041092/9e4b78fb-6f78-4390-8bd6-c9f8778ac7a2" />

  <br />
  <br />

  <p align="center">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
    <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" />
    <img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" />
    <img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white" />
    <img src="https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white" />
  </p>
</div>

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
