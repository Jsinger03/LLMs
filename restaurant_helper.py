import os
from secret_key import open_api_key

#I have the secret key setup as an environment variable
os.environ['OPENAI_API_KEY'] = open_api_key

from langchain.llms import OpenAI
app_llm = OpenAI(temperature = 0.7)
image_llm = OpenAI(temperature = 0.9)
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper


def gen_restname_menu(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables = ["cuisine"],
        template = "I want to open a restaurant fr {cuisine} food. Suggest a fancy name for this"
    )
    #create a chain - gather the template and llm request into 1 step via a chain (think of as a wrapper)
    chain_name = LLMChain(llm = app_llm, prompt = prompt_template_name, output_key = 'restaurant_name')

    #================================================================================================================

    prompt_template_menu = PromptTemplate(
        input_variables = ["restaurant_name"],
        template = "I want to open a restaurant called {restaurant_name}. Suggest menu items for this restaurant, but no more than 8 items on the menu, and at least one must be dessert. Return as a comma separated list"
    )

    chain_menu = LLMChain(llm = app_llm, prompt = prompt_template_menu, output_key = 'menu_items')


    chain = SequentialChain(
        chains = [chain_name, chain_menu],
        input_variables = ['cuisine'],
        output_variables = ['restaurant_name', 'menu_items']
        )

    response = chain({'cuisine' : "New American"})
    return response
from io import BytesIO

def gen_item_image(item):
    prompt_template_images = PromptTemplate(
        input_variables=["item"],
        template="Generate a prompt to create an image of the {item}. Provide only details pertaining to the plate and the dish.",
        length=1000  # Set the desired length value here
    )
    chain_image = LLMChain(llm=image_llm, prompt=prompt_template_images)
    prompt = chain_image.run(item)
    print(prompt)
    image_url = DallEAPIWrapper().run(prompt[:1000])
    import requests
    from PIL import Image
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    # image.show()
    return image