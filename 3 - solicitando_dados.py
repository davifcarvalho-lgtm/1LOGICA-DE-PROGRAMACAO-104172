import os

#limpa o terminal.
os.system("cls")

# SOLICITANDO DADOS.

#input adiciona o que for digitado ao terminal na variavel como texto.
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

#int() converte o que for digitado em inteiro (números inteiros).
idade = int(input("Digite sua idade: "))

#float() converte o que foi digitado em float (números reais).
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

# MOSTRANDO DADOS.
print("nome: ", nome)
print("sobrenome: ", sobrenome)
print("idade: ", idade)
print("peso: ", peso)
print("altura: ", altura)
            