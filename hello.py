import streamlit as st

st.title("bem vindo a minha primeira pagina weeb")
st.subheader("desenvolvido por: gabriel")

nome = st.text_input("digite seu nome: ")

if nome:
    st.write(f"bem vindo{nome}")
    st.baloons()