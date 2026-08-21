import os

#Limpa o terminal
os.system("cls")

print("= SOLICITANDO DADOS")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
primeira_nota = float(input("Digite a sua primeira nota: "))
segunda_nota = float(input("Digite a sua segunda nota: "))

print("\n= EXIBINDO DADOS =")
print("nome: ", nome)
print("idade: ", idade)
print("primeira nota ", primeira_nota)
print("segunda nota ", segunda_nota)


