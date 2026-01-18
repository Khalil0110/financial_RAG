import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle

class VectorStore:
    def __init__(self, index_path="data/index/faiss.index", meta_path="data/index/meta.pkl"):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index_path = index_path
        self.meta_path = meta_path
        self.texts = []

        os.makedirs("data/index", exist_ok=True)

        if os.path.exists(index_path) and os.path.exists(meta_path):
            self.index = faiss.read_index(index_path)
            with open(meta_path, "rb") as f:
                self.texts = pickle.load(f)
        else:
            self.index = faiss.IndexFlatL2(384)

    def add_texts(self, texts):
        embeddings = self.model.encode(texts)
        self.index.add(np.array(embeddings).astype("float32"))
        self.texts.extend(texts)

        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, "wb") as f:
            pickle.dump(self.texts, f)

    def search(self, query, k=5):
        q_emb = self.model.encode([query])
        _, indices = self.index.search(
            np.array(q_emb).astype("float32"), k
        )
        return [self.texts[i] for i in indices[0]]