#search.py
import os
from dotenv import load_dotenv
from src.vectore_store import FaissVectorStore
from langchain_groq import ChatGroq

load_dotenv()

class RAGSearch:
    def __init__(self, persist_dir: str = "faiss", embedding_model: str="all-MiniLM-L6-v2", llm_model ="gemma2-9b-it", temperature=0.1, max_tokens=1024):

        self.vectorstore= FaissVectorStore(persist_dir, embedding_model)
        # Load or build vectorstore
        faiss_path = os.path.join(persist_dir, "faiss.index") 
        meta_path= os.path.join(persist_dir, "metadata.pkl")
        if not (os.path.exists(faiss_path) and os.path.exists(meta_path)):
            from louder import loader
            docs =loader("data")
            self.vectore_store.build_from_documents(docs)
        else:
            self.vectore_store.load()
        groq_api_key = "use the api key of groq ai "
        self.llm =ChatGroq(groq_api_key= groq_api_key,model_name= llm_model)
        print(f" info Groq LLM initialize : {llm_model} ")
    
    def search_and_summarize(self, query: str, top_k: int = 5) -> str:
        results= self.vectore_store.query(query, top_k=top_k)
        texts = [r["metadata"].get("text", "") for r in results if r["metadata"]]
        context = "\n\n".join(texts)
        if not context:
            return " No relevant documents found"
        prompt= f""" Summarize the following context for the query: '{query}'\n\nContext:\n\n Answer:"""
        response =self.llm.invoke([prompt])
        return response.content
        