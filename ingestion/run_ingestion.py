from ingestion.load_data import load_pdfs
from ingestion.chunking import chunk_text
from ingestion.embed_store import VectorStore

vector_store = VectorStore()

docs = load_pdfs("data/amf")

for doc in docs:
    chunks = chunk_text(doc["text"])
    vector_store.add_texts(chunks)

print("AMF documents ingested successfully.")