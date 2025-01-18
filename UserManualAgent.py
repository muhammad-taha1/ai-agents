from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

import nest_asyncio
nest_asyncio.apply()

class UserManualAgent:

    def __init__(self):
        Settings.embed_model = OllamaEmbedding(model_name="all-minilm:22m")
        Settings.llm = Ollama(model="tinyllama", request_timeout=60*5)
        # Settings.chunk_size = 512
        # Settings.chunk_overlap = 50
        documents = SimpleDirectoryReader("docs/user_manuals").load_data(show_progress=True)
        index = VectorStoreIndex.from_documents(documents, show_progress=True)
        self.query_engine = index.as_query_engine()


    def query(self, question):
        print("user query: ", question)
        return self.query_engine.query(question)


if __name__ == "__main__":
    agent = UserManualAgent()
    response = agent.query("How to setup Roborock vacuum?")
    print(response)