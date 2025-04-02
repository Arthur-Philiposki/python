import streamlit as st
import datetime

nome = st.text_input("Qual o Nome: ") 
st.write("O nome digitado é: ", nome)

sobrenome = st.text_input("Qual o Sobrenome: ")
st.write("O sobrenome digitado é: ", sobrenome)

data = st.date_input("Quando é o Aniversario", value=None)
st.write("Aniversario é na data:", data)

option = st.selectbox(
    "Qual é o Estado civil? ",
    ("Solteiro", "Casado", "Divorciado", "Viúvo"),
    index=None,
    placeholder="Seleção.",
)
st.write("O estado civil selecionado é:", option)


option = st.selectbox(
    "Qual é o seu sexo? ",
    ("Masculino", "Feminino", "Outro"),
    index=None,
    placeholder="Seleção.",
)
st.write("O sexo selecionado é:", option)

salario = st.text_input("Qual o Salario: ")
st.write("O salario digitado é: ", salario)
