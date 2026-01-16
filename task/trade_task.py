from crewai import Task
from agents.trader_agent import trader_agent

trade_decision = Task(
    description=(
        "Based on the stock analysis provided, decide whether the stock should be "
        "Bought, Sold, or Held. Justify the decision clearly."
    ),
    expected_output=(
        "A clear decision of Buy, Sell, or Hold with concise reasoning."
    ),
    agent=trader_agent,
)
