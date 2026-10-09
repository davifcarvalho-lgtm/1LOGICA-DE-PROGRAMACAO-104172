soma = 0
quantidade = 0

print("Digite valores inteiros positivos (digite um número negativo para parar):")

while True:
    numero = int(input("Digite um número: "))
    if numero < 0:
        break
    soma += numero
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"\nMédia aritmética dos números informados: {media:.2f}")
else:
    print("\nNenhum número positivo foi informado.")