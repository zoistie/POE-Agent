from apikey import apikey
import os
from langchain.agents import AgentType, initialize_agent
from langchain.llms import OpenAI
from tools import sendgmailtool, maketxttool


os.environ['OPENAI_API_KEY'] = apikey
llm = OpenAI(temperature = 0.9)

tools = [sendgmailtool,maketxttool]

agent = initialize_agent(
    tools, llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose = True,handle_parsing_errors=True)
prompt = "send an email to nyuichi03@gmail.com, with a subject as hummus and attach hummus.jpg to the body of the email"
response = agent.run(prompt)
print(response)
