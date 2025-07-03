from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.7, max_tokens=200)
    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="You are a {animal_type} name generator. My pet is {pet_color} in color. Generate 5 unique and creative names for a pet {animal_type}.",
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)
    response = name_chain({'animal_type': animal_type, 'pet_color': pet_color})

    return response

if __name__ == "__main__":
    pet_name = generate_pet_name("cow", "black")
    print(f"Generated pet name: {pet_name}")