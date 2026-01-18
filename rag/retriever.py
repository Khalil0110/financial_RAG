class Retriever:
    def __init__(self, vector_store, top_k=5):
        self.vector_store = vector_store
        self.top_k = top_k

    def retrieve(self, query):
        """
        Retrieve relevant document chunks for a query.

        Parameters
        ----------
        query : str

        Returns
        -------
        list[str]
            Retrieved text chunks
        """
        return self.vector_store.search(query, k=self.top_k)