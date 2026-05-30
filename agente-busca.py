from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.tavily import TavilyTools
from agno.db.sqlite import SqliteDb

#todos agentes necessarios da chav de API, e a função LOAD_DOTENV faz a leitura do arquivo no .env.
load_dotenv()

bancoDados = SqliteDb(db_file="temp/registros.db")

agente = Agent(
    #essa linha define o modelo do meu agente
    model=OpenAIChat(id="gpt-4o-mini"),
    description="tenha a personalidade de um velho ranzinza",
    add_culture_to_context=True,
    db=bancoDados,
    tools=[DuckDuckGoTools(),TavilyTools],
    markdown=True
)
while True:
    pergunta = input("Digite a sua pergunta: ")
    if pergunta.lower() in ["exit","sair","quit"]:
        print("encerrando o agente...\nFique avontade quando tiver mais duvidas")
        break
    else:
        agente.print_response(pergunta)