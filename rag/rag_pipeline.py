from rag.prompt import build_prompt

class RAGPipeline:
    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm

    def answer(self, question):
        context_docs = self.retriever.retrieve(question)
        prompt = build_prompt(question, context_docs)
        return self.llm(prompt)