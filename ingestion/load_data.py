import pdfplumber
from pathlib import Path

def load_pdfs(folder_path):
    docs = []
    for pdf_path in Path(folder_path).glob("*.pdf"):
        with pdfplumber.open(pdf_path) as pdf:
            text = "\n".join(page.extract_text() or "" for page in pdf.pages)
            docs.append({
                "text": text,
                "source": pdf_path.name
            })
    return docs