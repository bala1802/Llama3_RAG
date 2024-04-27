import gradio as gr
from rag import rag_chain

def process_request():
    iface = gr.Interface(
    fn=rag_chain,
    inputs=["text", "text"],
    outputs="text",
    title="RAG using Llama 3",
    description="Provide a URL along with a query to retrieve answers from the RAG chain.")
    
    iface.launch()

if __name__ == "__main__":
    process_request()