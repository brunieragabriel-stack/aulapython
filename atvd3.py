import streamlit as st

st.title("Pizaaria Dipadre")
st.subheader("Coloque sua informções para podermos chegar o mais perto de você")
st.image("pizza.jpg",width=500)
nome = st.text_input("Digite seu nome: ")

cidade = st.text_input("Nós informe sua cidade: ")

bairro = st.text_input("Agora digamos seu bairro: ")

pizzasDisponiveis = st.selectbox("Pizzas Disponíveis",["Calabresa","Margherita","Portuguesa","Quatro Queijos"])
aceitatermos = st.checkbox("Ao clicar aqui você aceitara os termos de nossa pizzaria")

if st.button("envie seu pedido"):
    if nome and cidade and bairro and pizzasDisponiveis and aceitatermos:
        st.success()
    else:
        st.error()
