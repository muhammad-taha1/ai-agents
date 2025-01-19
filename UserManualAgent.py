from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool

import nest_asyncio
nest_asyncio.apply()
import time

class UserManualAgent:

    def __init__(self):
        Settings.embed_model = OllamaEmbedding(model_name="all-minilm:22m")
        Settings.llm = Ollama(model="llama3.1", request_timeout=60*5)
        Settings.chunk_size = 700
        Settings.chunk_overlap = 20
        documents = SimpleDirectoryReader("docs/user_manuals").load_data(show_progress=True)
        index = VectorStoreIndex.from_documents(documents, show_progress=True)
        query_engine = index.as_query_engine(similarity_top_k=4)
        user_manual_query_tool = QueryEngineTool.from_defaults(
            query_engine, 
            name="user_manual_query_tool",
            description=(
                "A RAG engine with of various user manuals of appliances.",
                "Use a detailed plain text question as input to the tool.")
            )
        
        self.agent = ReActAgent.from_tools(
            [user_manual_query_tool],
            verbose=True,
            system_prompt="""
               You are a helpful agent designed to answer queries about various appliances from user manuals.
               Always use tools provided to answer the queries, and do not rely on prior knowledge.
               Try to be as consice as possible in your responses.
            """,
            )


    def query(self, question):
        print("user query: ", question)
        start_time = time.time()
        response = self.agent.chat(question)
        response_time = time.time() - start_time
        print("response time: ", response_time)
        return response


if __name__ == "__main__":
    agent = UserManualAgent()
    response = agent.query("How often should i change the filter and clean the sensors of the Roborock vacuum?")
    print(response)