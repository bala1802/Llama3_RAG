# Llama3 - Retrieval-Augmented Generation
Implementation of Llama3's RAG model utilizing Ollama

## Purpose

The purpose of this repository is to facilitate the understanding and implementation of a chatbot application based on the RAG (Retrieval-Augmented Generation) architecture. It utilizes the Llama-3 Large Language Model with the assistance of Ollama to achieve this goal.

## Repository Architecture

```
.
├── LICENSE
├── README.md
├── app.py
├── config.py
├── data_loader.py
├── data_utils.py
├── flagged
│   └── log.csv
└── rag.py
```

## Ollama

Ollama is a powerful tool that simplifies the process of creating, running, and managing language models through a straightforward API. With Ollama, developers can seamlessly integrate pre-built models into their applications, enhancing functionality and accelerating development.

### Installation

- Command line installation  `curl -fsSL https://ollama.com/install.sh | sh`
- Download from [Ollama](https://ollama.com/download)

### Run Ollama

`ollama run llama3`

The llama3 service will be hosted at the following address: http://localhost:11434.

## Application

This application encompasses four distinct subtasks.

### 1. Data Loader 

`data_loader.py`

In this context, a web URL serves as the corpus for the chatbot. Data is extracted directly from the URL. Applied a Chunking Strategy to segment the data into smaller, meaningful chunks. These chunks are then converted into embeddings and stored within the Chroma DB for efficient retrieval and processing.

### 2. Generate Embeddings and Vector DB Storage

`data_loader.py`

I utilized `nomic-embed-text` to generate embeddings from the input data. These embeddings are subsequently stored within the ChromaDB

### 3. Initialize Ollama Model

`model.py`

The Llama3 model is initialized through Ollama.

### 4. Retrieval-Augmented Generation

`rag.py`

Responsible for triggering the retriever to extract pertinent chunks for responding to the user's query. The formatted prompt will be,

```
Question: {user_query}
Context: {context}
```

## Chatbot

Run `python app.py` to lauch the user interface

## Output

<img width="1246" alt="image" src="https://github.com/bala1802/Llama3_RAG/assets/22103095/04d56c1b-ad7e-4385-8cdc-c19c7b8d1402">
