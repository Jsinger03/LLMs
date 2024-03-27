import os
from secret_key import open_api_key, serp_api_key

#Set up python file with the keys
os.environ['OPENAI_API_KEY'] = open_api_key
os.environ['SERPAPI_API_KEY'] = serp_api_key #get from SerpAPI, free for 100 searches per month

from langchain.llms import OpenAI
app_llm = OpenAI(temperature = 0.7)#temperature is a var between 0 and 1, determinesthe level of creativity of response

#create an Agent (wrapper for one or more tools)
from langchain.agents import AgentType, initialize_agent, load_tools

tools = load_tools(["serpapi", "llm-math"], llm = app_llm)
agent = initialize_agent(
    tools,
    app_llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose = True #see how the agent thinks, default is False
)

response = agent.run("What was the number of Ferraris sold in 2023? Add 5 to the result")
print(response)