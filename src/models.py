from langchain.llms import LlamaCpp
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_groq import ChatGroq

def hf_embeddings():
    return HuggingFaceEmbeddings(
        model_name = "sentence-transformers/all-mpnet-base-v2",
    )

def code_llama():
    
    llm =ChatGroq(model_name="mixtral-8x7b-32768", temperature=0.7,groq_api_key="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")

    return llm