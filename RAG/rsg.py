import numpy as py
import faiss
import json
from sentence_transformers import SentenceTransformer
from Llm.groq_runtime import GroqRunTime

class RAG: 
    def __init__(self, database_name):
        self.index = faiss.read_index("datasets/{database_name}index.faiss")