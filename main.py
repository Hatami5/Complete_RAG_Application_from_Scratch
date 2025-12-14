#main.py
from src.louder import loader
from src.embedding import EmbeddingManager
from src.vectore_store import FaissVectorStore
from src.search import RAGSearch


if __name__ == "__main__":
   # load = loader("data")  # when first time load then comment it
  #  chunk = EmbeddingManager.chunk_document(load)
  #  vector_emb =EmbeddingManager.generate_embedding(chunk)
     store= FaissVectorStore("faiss")
      # store.build_from_documents(load) #build file one time then  comment it
     store.load() # After we loading the file then we need to load file 
   # print(store.query("What is attention mechanism?", top_k=3))

     rag_search = RAGSearch()
     query ="What is attention mechanism?"
     summmary = rag_search.search_and_summarize(query,top_k=3)
     print("Summary", summmary)
