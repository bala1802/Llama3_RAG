import data_loader as data_loader
import data_utils as data_utils
import config as config

import ollama

def rag_chain(url, question):
    retriever = data_loader.load_and_retrieve_docs(url)
    retrieved_docs = retriever.invoke(question)
    formatted_context = data_utils.format_docs(retrieved_docs)
    formatted_prompt = f"Question: {question}\n\nContext: {formatted_context}"
    response = ollama.chat(model=config.LLAMA3_MODEL, messages=[{'role': 'user', 'content': formatted_prompt}])
    
    return response['message']['content']