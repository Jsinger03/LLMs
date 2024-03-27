import os
from secret_key import open_api_key, serp_api_key

#Set up python file with the keys
os.environ['OPENAI_API_KEY'] = open_api_key

from langchain.llms import OpenAI
app_llm = OpenAI(temperature = 0.7)#temperature is a var between 0 and 1, determinesthe level of creativity of response

#create an Agent (wrapper for one or more tools)
from langchain.agents import AgentType, initialize_agent, load_tools

tools = load_tools(["wikipedia", "llm-math"], llm = app_llm)
agent = initialize_agent(
    tools,
    app_llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose = True #see how the agent thinks, default is False
)

response = agent.run("When was Elon Musk born? WHat is his age now in 2024?")
print(response)