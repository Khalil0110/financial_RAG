# Financial RAG: Retrieval-Augmented Generation for Financial Documents
This project implements a **RAG pipeline** for analyzing financial documents using **open-source LLMs and vector search**.  
It allows users to ask natural-language questions and receive **grounded answers** from documents like annual reports, risk disclosures, and earnings call transcripts.

---
## Features
- **Document ingestion**: PDF / text parsing and chunking
- **Vector store**: FAISS embeddings for fast semantic search
- **LLM answering**: Local, open-source model (Mistral via Ollama)
- **Synthetic financial documents included** for testing
- **Grounded answers**: avoids hallucinations; cites source text
- **CLI interface** via `app/app.py`

---
## Setup
### 1. Clone the repo
git clone https://github.com/Khalil0110/financial_RAG/
### 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
### 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
### 4. Ingest documents
python ingestion/run_ingestion.py
### 5. Run the interactive app
python -m app.app

