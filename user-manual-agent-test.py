from typing import Optional
from phi.agent import Agent, RunResponse
from phi.model.ollama import Ollama
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.knowledge.agent import AgentKnowledge
from phi.vectordb.chroma import ChromaDb
from rich.prompt import Prompt
from phi.embedder.ollama import OllamaEmbedder
from phi.document.chunking.fixed import FixedSizeChunking
import typer
from PdfExtractor import PdfExtractor
 


vector_db = ChromaDb(
    collection="user_manuals",
    embedder=OllamaEmbedder(id="nomic-embed-text"),    
)

knowledge_base = AgentKnowledge(
    vector_db= vector_db)

# get user manual text
text_files = PdfExtractor().extract_pdf_text_from_directory("./docs/user_manuals")

for text in text_files:
    knowledge_base.load_text(text)


agent = Agent(
    use_tools=True,
    show_tool_calls=True,
    debug_mode=True,
    model=Ollama(id="llama3.1"),
    markdown=True,
    knowledge_base=knowledge_base,
    search_knowledge=True,
    description="You are an AI agent for answering relevant questions from the user manuals in your knowledge base and the provided information",
    instructions=[
        "When a user asks a question, you will be provided with information about the question.",
        "Carefully read this information and provide a clear and concise answer to the user.",
        "Do not use phrases like 'based on my knowledge' or 'depending on the information'.",
        "Provide a direct answer to the user's question, based on the knowledge you have from knowledge base.",
    ],
    add_references_to_prompt=True,
    add_datetime_to_instructions=True,
)

   
    
agent.print_response("How to clean aerogarden pump?", stream=True)