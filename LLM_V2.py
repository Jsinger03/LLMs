import os
from secret_key import open_api_key

#I have the secret key setup as an environment variable
os.environ['OPENAI_API_KEY'] = open_api_key

from langchain.llms import OpenAI
app_llm = OpenAI(temperature = 0.7)#temperature is a var between 0 and 1, determinesthe level of creativity of response

from langchain.prompts import PromptTemplate
prompt_template_name = PromptTemplate(
    input_variables = ["cuisine"],
    template = "I want to open a restaurant fr {cuisine} food. Suggest a fancy name for this"
)
prompt_name = prompt_template_name.format(cuisine = "Mexican")
#prompt time: Working with LLMs and prompt framework
name = app_llm(prompt_name)
print(name)


