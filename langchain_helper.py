from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain.agents import load_tools
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.7, max_tokens=200)
    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="You are a {animal_type} name generator. My pet is {pet_color} in color. Generate 5 unique and creative names for a pet {animal_type}.",
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='pet_name')
    response = name_chain({'animal_type': animal_type, 'pet_color': pet_color})

    return response

def langchain_agent():
    llm = OpenAI(temperature=0.7, max_tokens=200)
    tools = load_tools(["wikipedia", "llm-math"], llm=llm)
    
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    result = agent.invoke("What is the average age of a dog? Add 5 to it.")
    
    print(result)

if __name__ == "__main__":
    langchain_agent()
    # pet_name = generate_pet_name("cow", "black")
    # print(f"Generated pet name: {pet_name}")

