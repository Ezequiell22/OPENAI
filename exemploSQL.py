from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_openai import ChatOpenAI
from langchain_community.utilities.sql_database import SQLDatabase
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

db = SQLDatabase.from_uri('postgresql://postgres:root@127.0.0.1:5432/floresnew15')

chat = ChatOpenAI(model='gpt-3.5-turbo-0125')

agent_executor = create_sql_agent(
    chat,
    db=db,
    verbose=True
)

result = agent_executor.invoke({'input': 'qual o nome da banco de dados?'})
print(result)