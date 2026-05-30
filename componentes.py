import streamlit as st

st.title("Secretaria SENAI Americana")
st.subheader("Conheça os nossos cursos")

st.write("I.A Generativa, porfavor BI, empilhadeira, excel, eletricista instalador")
st.markdown("**Atenção** : verifique se existem vagas disponíveis.")

nome = st.text_input("Digiteo seu nome: ")
idade = st.number_input("digite sua idade", min_value=16, max_value=99)
cursoEscolhido = st.selectbox("Cursos dsponíveis", ["I.A. Generativa","Power BI","Empilhadeira","Excel","eletricista instalador"])
aceitatermos = st.checkbox("Ao clicar aqui, você aceita os termos e condições")

if st.button("Enviar resposta"):
    if nome and idade and cursoEscolhido and aceitatermos:
        st.success()
    else:
        st.error()