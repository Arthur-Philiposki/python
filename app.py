import streamlit as st
import datetime

nome = st.text_input("Qual o Nome: ") 
st.write("O nome digitado é: ", nome)

sobrenome = st.text_input("Qual o Sobrenome: ")
st.write("O sobrenome digitado é: ", sobrenome)

data = st.date_input("Quando é o Aniversario", value=None)
st.write("Aniversario é na data:", data)

Estado = st.selectbox(
    "Qual é o Estado civil? ",
    ("Solteiro", "Casado", "Divorciado", "Viúvo"),
    index=None,
    placeholder="Seleção.",
)
st.write("O estado civil selecionado é:", Estado)


option = st.selectbox(
    "Qual é o seu sexo? ",
    ("Masculino", "Feminino", "Outro"),
    index=None,
    placeholder="Seleção.",
)
st.write("O sexo selecionado é:", option)

salario = st.number_input("Qual o Salario: ")
st.write("O salario digitado é: ", salario)

if (salario < 2500):
    st.write("Funcionario precisa receber aumento")

else:
    st.write("Funcionario NÃO precisa de aumento")

# aumento = 0
# for i in range(5):
#     aumento += 100

aumento = 0
while aumento < 500:
    aumento += 100
    
    st.write (aumento)
    
salario += aumento

st.write (salario)
