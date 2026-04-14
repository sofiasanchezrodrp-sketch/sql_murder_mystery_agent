from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_anthropic import ChatAnthropic
from langchain.tools import tool
from langchain_community.utilities import SQLDatabase
from langchain.messages import HumanMessage

load_dotenv()

# Conectar a la base de datos
db = SQLDatabase.from_uri("sqlite:///database/sql-murder-mystery.db")

# Definir la tool SQL
@tool
def sql_query(query: str) -> str:
    """Execute a SQL query against the murder mystery database and return the results."""
    try:
        return db.run(query)
    except Exception as e:
        return f"Error: {e}"

# Crear el modelo y el agente
model = ChatAnthropic(model="claude-haiku-4-5", temperature=0.1)
agent = create_agent(model=model, tools=[sql_query])

# Lanzar al agente
response = agent.invoke({
    "messages": [HumanMessage(content="""
        A crime has taken place and the detective needs your help. 
        The crime was a murder that occurred sometime on Jan.15, 2018 in SQL City.
        Start by retrieving the schema of the database, then find the crime scene report,
        and follow the clues to identify the murderer.
    """)]
})

print(response['messages'][-1].content)