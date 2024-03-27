import os
from secret_key import open_api_key, serp_api_key

#Set up python file with the keys
os.environ['OPENAI_API_KEY'] = open_api_key

from langchain.llms import OpenAI
app_llm = OpenAI(temperature = 0.7)#temperature is a var between 0 and 1, determinesthe level of creativity of response

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(k=1)

convo = ConversationChain(llm = app_llm, memory=memory)
print(convo.run("Who won the first NBA championship?"))
print(convo.run("Who was the first F1 world champion of this millenium?"))
print(convo.run("what is 5^55?"))
print(convo.run("Who won the MVP that year?"))
