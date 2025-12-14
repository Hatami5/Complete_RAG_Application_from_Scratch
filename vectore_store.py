#vector_store.py
import os
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List, Any, Tuple, Dict
from src.embedding import EmbeddingManager


class FaissVectorStore:
    def __init__(self, persist_directory ="faiss", embedding_model: str ="all-MiniLM-L6-v2", chunk_size: int = 1000, chunk_overlap: int= 300):
        self.persist_directory =persist_directory
        os.makedirs(persist_directory, exist_ok=True)
        self.index= None
        self.metadata =[]
        self.embedding_model = embedding_model
        self.chunk_overlap =chunk_overlap
        self.chunk_size = chunk_size
        print("[Embeddig ] model loaded")

    def build_from_documents(self, documents: List[Any]):
        print(f"INFO Building vector store from {len(documents)} raw documents....")
        emb_pipe= EmbeddingManager(model_name=self.embedding_model, chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        chunks =emb_pipe.chunk_document(documents)
        embeddings =emb_pipe.generate_embedding(chunks)
        metadatas=[{"text": chunk.page_content} for chunk in chunks]
        self.add_embeddings(np.array(embeddings).astype('float32'), metadatas)
        self.save()
        print(f"Vector store built and saved to{self.persist_dir}")

    def add_embeddings(self, embeddings: np.ndarray, metadatas: List[Any] = None):
        dim =embeddings.shape[1]
        if self.index is None:
            self.index= faiss.IndexFlatL2(dim)
            self.index.add{embeddings}
        if metadatas:
            self.metadata.extend(metadatas)
        print(f"added {embeddings.shape[0]} vector to fiass index.")

    def save(self):
        faiss_path = os.path.join(self.persist_dir, "faiss.index")
        meta_path = os.path.join(self.persist_dir, "metadata.pkl")
        faiss.write_index(self.index, faiss_path)
        with open(meta_path, "wb") as f:
            pickle.dump(self.metadata, f)
        print(f" saved faiss index and metadata to {self.persist_dir}")
    def load(self):
        faiss_path= os.path.join(self.persist_dir, "faiss.index")
        meta_path = os.path.join(self.persist_dir, "metadata.pkl")
        self.index = faiss.read_index(faiss_path)
        with open(meta_path, "rb") as f:
            self.metadata = pickle.load(f)
        print(f"loaded fiass index and metadata")
    def search(self, query_embedding: np.ndarray, top_k: int=5):
        D, I = self.index.search(query_embedding, top_k)
        results= []
        for idx, dist in zip(I[0], D[0]):
            meta = self.metadata[idx] if idx< len(self.metadata) else None
            results.append({"index": idx, "distance": dist, "metadata": meta})
        return results
    def query(self, query_text: str, top_k: int = 5):
        print(f" Info querying vector store for :'{query_text}' ")
        query_emb = self.model.encode([query_text]).astype('float32')
        return self.search(query_emb, top_k=top_k)
    
              


