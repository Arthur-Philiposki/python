import streamlit as st

st.header ("Atividade Python")

st.toggle ("Toggle")

st.text_input ("Adicione o Nome: ")
st.text_input ("Adicione o Sobrenome: ")
st.text_input ("Adicione a Data de nascimento: ", "Exemplo: xx/xx/xxxx")
st.text_input ("Adicione o Salario: ")

st.selectbox (
  'Qual o Estado civil: ', 
  ('Solteiro', 'Casado', 'Divorciado', 'Viúvo'))

st.selectbox (
  'Qual o Sexo: ', 
  ('Masculino', 'Feminino', 'Outro'))
