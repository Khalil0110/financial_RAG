def build_prompt(question, context_docs):
    context = "\n\n".join(context_docs)

    return f"""
You are a financial analyst assistant.
Answer ONLY using the information provided below.
If the answer is not in the documents, say "Not found in the documents".

Documents:
{context}

Question:
{question}

Answer:
"""