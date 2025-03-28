import streamlit as st
import datetime

nome = st.text_input("Qual o Nome: ")
st.write("O nome digitado é: ", nome)

sobrenome = st.text_input("Qual o Sobrenome: ")
st.write("O sobrenome digitado é: ", sobrenome)

data = st.date_input("Quando é o Aniversario", value=None)
st.write("Aniversario é na data:", data)
