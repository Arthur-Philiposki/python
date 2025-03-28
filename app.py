import streamlit as st

Aluguel = int(input ("Qual o valor do Aluguel? "))
Energiaeletric = int(input ("Qual o valor da Energia Eletrica? "))
Intern = int(input ("Qual o valor da Internet? "))
Agua = int(input ("Qual o valor da Água? "))

fixo = Aluguel + Energiaeletric + Intern + Agua

print ("")
print (f"Custo Fixo é: {fixo}")
print ("")

Condensado = int(input ("Valor da Lata de leite condensado (395g)? "))
Ovos = int(input ("Valor de Ovos? "))
Trigo = int(input ("Valor de Xícara de farinha de trigo (120)? "))
Gas = int(input ("Valor de Gás? "))
Embalagem = int(input ("Valor de Embalagem? "))

variavel = Condensado + Ovos + Trigo + Gas + Embalagem
print ("")
print (f"Custo variável é: {variavel}")
print ("")

Cozinha = int(input ("Qual o valor da cozinha? "))
Vendas = int(input ("Qual o valor das Vendas? "))
Administrativo = int(input ("Qual o valor Administrativo? "))
Dominio = int(input ("Qual o valor Dominio? "))
Mei = int(input ("Qual o valor MEI? "))
Transporte = int(input ("Qual o valor transporte? "))
Valorembalagem = int(input ("Qual o valor de Embalagem? "))

despesa = Cozinha + Vendas + Trigo + Administrativo + Dominio + Mei + Transporte + Valorembalagem
print ("")
print (f"Custo variável é: {despesa}")
print ("")

imposto = int(input ("Qual o valor do Imposto? "))

print ("")
print (f"Custo variável é: {imposto}")
print ("")



