import streamlit as st
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools

load_dotenv()

agente = Agent (#Tupla pois não mudaremos os parâmetros do agente
model=OpenAIChat(id="gpt-4o-mini"),
description="Vcê é um hiscritor que já ganhou diversoso prêmios por suas obras literarias e agora você cria historias baseadas no gosto de seus clintes",
tools=[DuckDuckGoTools(),WikipediaTools()],
markdown=True
)

st.title("Agente de I.A. 🤖")

pergunta = st.chat_input("me diga alguma coisa")

if pergunta:
    
    with st.chat_message("user"):
        st.markdown(pergunta)
    with st.chat_message("assistant"):
     with st.spinner("Agente pensando..."):
        resposta = agente.run(pergunta)
        st.markdown(resposta.content)
        