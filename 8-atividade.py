#limpa o terminal
import os
os.system

#Entrada
print("=SOLICITANDO DADOS =")
primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o segundo numero: "))

#processamento
media = (primeiro_numero * segundo_numero)

#saida
print("primeiro_numero: ", primeiro_numero)
print("segundo numero: ", segundo_numero)
print("media ", media)

if media >=7:
    print("maior")
else:
    print("menor") 