from crewai import Task
from agents.analyst_agent import analyst_agent

get_stock_analysis = Task(
    description=(
        "Analyze the recent performance of the stock: {stock}. "
        "Use the live stock information tool to retrieve the current price "
        "and daily change. Provide a concise summary of today's performance."
    ),
    expected_output=(
        "A bullet-point summary including:\n"
        "- Current stock price\n"
        "- Daily price change and percentage\n"
        "- Short performance insight"
    ),
    agent=analyst_agent,
)
