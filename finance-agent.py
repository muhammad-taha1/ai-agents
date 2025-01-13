from phi.agent import Agent, RunResponse
from phi.model.ollama import Ollama
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

stock_agent = Agent(
    name="Crypto finance Agent",
    role="Analyze and present financial data",
    model=Ollama(id="llama3.1"),
    markdown=True,
    tools=[YFinanceTools(stock_price=True, key_financial_ratios=True,  analyst_recommendations=True, technical_indicators=True)],
        instructions=[
        "Use tables to display numerical data",
        "Include key financial metrics and trends",
        "Provide context for financial recommendations",
        "Analyze technical indicators for trading signals",
    ],
    show_tool_calls=True,
    monitoring=True
)

research_agent = Agent(
    name="Crypto research Agent",
    role="Search the web for accurate and up-to-date information",
    model=Ollama(id="llama3.1"),
    markdown=True,
    tools=[DuckDuckGo(search=True, news=True)],
        instructions=[
        "Always include sources and citations",
        "Verify information from multiple sources when possible",
        "Present information in a clear, structured format",
    ],
    show_tool_calls=True,
    monitoring=True
)

# Get the response in a variable
# run: RunResponse = agent.run("Share a 2 sentence horror story.")
# print(run.content)

# Print the response in the terminal
multi_agent = Agent(
    name="Crypto trading Agent",
    team=[stock_agent, research_agent],
    model=Ollama(id="llama3.1"),
    markdown=True,
    instructions=[
        "Always include sources and citations",
        "Use tables to display structured data",
                     "Combine financial data with relevant market news",
        "Provide comprehensive analysis using both agents' capabilities"],
    show_tool_calls=True,
    monitoring=True
)

multi_agent.print_response("Summarize analyst recommendations and share the latest news for BTC-USD", stream=True)