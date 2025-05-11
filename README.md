# rag app from notebook to production 

This is a minimal implementation of the RAG model for question answering.

## Requirements

-Python 3.8 or later

#### Install Python using MiniConda
1) Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)

2) Create a new environment using the following command:
```bash
$ conda create -n rag-app python=3.8
```
3) Activate the environment using the following command:
```bash
$ conda activate rag-app
```

## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `GROQ_API_KEY` value.

you can find your API key in the [Groq dashboard](https://console.groq.com/keys).

## Run the FastAPI server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## POSTMAN Collection

Download the POSTMAN collection from [/assets/rag-app.postman_collection.json](/assets/rag-app.postman_collection.json)
