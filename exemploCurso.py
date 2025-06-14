from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

db = SQLDatabase.from_uri('sqlite:///banco.db')

chat = ChatOpenAI(model='gpt-3.5-turbo-0125')

agent_executor = create_sql_agent(
    chat,
    db=db,
    agent_type='tool-calling',
    verbose=True
)

agent_executor.invoke({'input': 'descreva o banco de dados'})

