#limpa o terminal
import os
os.system

#Entrada
print("=SOLICITANDO DADOS =")
primeira_nota = int(input("Digite a primeira nota: "))
segunda_nota = int(input("Digite a segunda nota: "))
terceira_nota = int(input("Digite a terceira nota: "))

#processamento
media = (primeira_nota + segunda_nota + terceira_nota) /3

    #Saida
print(" primeira nota: ",primeira_nota)
print(" segunda nota: ",segunda_nota)
print("terceira nota: ",segunda_nota)
print("media", media)
print("FIM DO PROGRAMA") 

if media >= 7:
    print("Aprovado! ")
else:
    print("Reprovado... ")
