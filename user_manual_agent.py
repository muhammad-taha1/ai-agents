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
        Settings.llm = Ollama(model="gemma2:2b", request_timeout=60*5)
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
        
        system_prompt = """
               System prompt:

               You are an AI assistant specialized in answering questions about appliances using information from user manuals. 

                1. Always rely on the **user_manual_query_tool** to retrieve information; do not use prior knowledge.
                2. If a query cannot be answered using the tool, respond with: "I cannot find this information in the user manuals provided."
                3. Do not attempt to generate answers without using the tool.
                4. Keep responses concise and directly answer the query.

                Note: The tool name is **user_manual_query_tool**, and it should be used for all queries.
            """
        
        self.agent = ReActAgent.from_tools(
            [user_manual_query_tool],
            verbose=True,
            system_prompt=system_prompt,
            )
        
        # print(self.agent.chat(system_prompt))
        
        
        print("done initializing agent")


    def query(self, question):
        print("user query: ", question)
        start_time = time.time()
        response = self.agent.stream_chat(question)
        response_time = time.time() - start_time
        print("response time: ", response_time)
        return response


if __name__ == "__main__":
    agent = UserManualAgent()
    response = agent.query("Which pastas can i make with kitchenaid pasta maker attachments?")


    print(response)