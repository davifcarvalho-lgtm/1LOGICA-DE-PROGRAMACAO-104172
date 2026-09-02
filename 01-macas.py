import os 
os.system("cls")

#ENTRADA.
quantidade=int(input("Digite a quantidade desejada: "))

#PROCESSAMENTO
if quantidade < 12:
    preco = quantidade = 1.30
else:
    preco = quantidade = 1.0

#SAIDA
print(f"valor total da compra: {valor_total:.2f})")