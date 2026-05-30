import streamlit as st
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools

load_dotenv()


personalidade = st.sidebar.selectbox("personalidade",["especialista em alimentação saudável","especialista em exercícios físicos","especialista em bem-estar mental"])

descricao = {
    
    "especialista em alimentação saudável":"Você é um especialista em alimentação saudável sugere receitas e refeições equilibradas",
    "especialista em exercícios físicos":"Você é um especialista em exercícios físicos monta treinos e dá dicas de musculação e cardio.",
    "especialista em bem-estar mental":"Você é um especialista em bem-estar mental dá dicas de gerenciamento de estresse e ansiedade"
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
            
st.title("Clinica Monismo")
            
pergunta = st.chat_input("pergunte ao seu formador")

if pergunta:
                
    with st.chat_message("user"):
        st.markdown(pergunta)
                    
    st.session_state.mensagem.append({"role":"user","content":pergunta})
                    
    with st.chat_message("assistant"):
        resposta = agente.run(pergunta)
        st.markdown(resposta.content)
                        
    st.session_state.mensagem.append({"role":"assistant","content":resposta.content})