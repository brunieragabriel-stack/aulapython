import streamlit as st

st.title("cadastro RH já")
st.subheader("sistema de cadrasto do RH")

nome = st.text_input("digite seu nome: ")

idade = st.text_input("digite sua idade")

email = st.text_input("digite seu email: ")

if nome and email and idade:
    st.success(f"acesso liberado")
    st.snow()
else:
    st.error("você precise preencher as informações acimas")