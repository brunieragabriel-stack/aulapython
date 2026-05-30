import streamlit as st
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools

load_dotenv()


personalidade = st.sidebar.selectbox("personalidade",["professor de python","professor de historia","cientista maluco"])

descricao = {
    
    "professor de python":"Você é um professor de python que responde com exemplos e contexto",
    "professor de historia":"Você é um professor de historia que ensina de forma clara, simples e objetiva.",
    "cientista maluco":"Você é um centista maluco que sempre está em busca de novas inovações e projetos"
}

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description= descricao [personalidade],
    tools=[DuckDuckGoTools(),WikipediaTools()],
    markdown=True
    
)

if "mensagens" not in st.session_state:
    st.session_state.mensagem = []
    
for msg in st.session_state.mensagem:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        
if st.sidebar.button("limpar conversas"):
    st.session_state.mensagem = []
    st.rerun()
            
st.title("sistema MultiAgentes")
            
pergunta = st.chat_input("pergunte ao agente")

if pergunta:
                
    with st.chat_message("user"):
        st.markdown(pergunta)
                    
    st.session_state.mensagem.append({"role":"user","content":pergunta})
                    
    with st.chat_message("assistant"):
        resposta = agente.run(pergunta)
        st.markdown(resposta.content)
                        
    st.session_state.mensagem.append({"role":"assistant","content":resposta.content})