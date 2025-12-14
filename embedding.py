#embedding.py
from typing import List, Any
from langchain.text_splitter import RecursiveCharacterTextSplitterharacter
import numpy as np
from src.louder import loader
class EmbeddingManager:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2", chunk_size: int =1000, chunk_overlap: int=300):
        
        self.model_name = model_name
        self.model =SentenceTransformer(model_name)
        print("Model Loaded Successfully ")
    def chunk_document(self, documents: List[Any])->List[Any]:
        splitter= RecursiveCharacterTextSplitter(
            chunk_size= self.chunk_size,
            chunk_overlap = self.chunk_overlap
            length_function =len
            separators=["\n\n", "\n", " ", ""]
        )
        chunks= splitter.split_documents(documents)
        print("sucessfully splite the document into chunks")
        return chunks
    def generate_embedding(self, chunks: List[str]) -> np.ndarray:
        if not self.model:
            raise ValueError("Model are not loaded ")
        text =[chunk.page_content for chunk in chunks]

        embeding = self.model.encode(text, show_progress_bar = True)

        print(" embedding generate successfully with: {embeding.shape} ")

        return embeding
    