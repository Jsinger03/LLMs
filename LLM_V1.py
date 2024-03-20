import os
from secret_key import open_api_key

#I have the secret key setup as an environment variable
os.environ['OPENAI_API_KEY'] = open_api_key

from langchain.llms import OpenAI
app_llm = OpenAI(temperature = 0.7)#temperature is a var between 0 and 1, determinesthe level of creativity of response

#prompt time: Working with LLMs in this framework
name = app_llm("I want to open a restaurant for Italian food. Suggest a fancy name for this")
print(name)


