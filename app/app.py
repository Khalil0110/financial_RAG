from ingestion.embed_store import VectorStore
from rag.retriever import Retriever
from rag.rag_pipeline import RAGPipeline
from llm.llm import call_llm

def main():
    print("Loading vector store...")
    vector_store = VectorStore()

    retriever = Retriever(vector_store, top_k=5)
    rag = RAGPipeline(retriever, call_llm)

    print("Financial RAG ready. Type 'exit' to quit.\n")

    while True:
        question = input("Question: ")
        if question.lower() in ["exit", "quit"]:
            break

        answer = rag.answer(question)
        print("\nAnswer:")
        print(answer)
        print("-" * 50)

if __name__ == "__main__":
    main()