pares = 0
impares = 0
soma_pares = 0
soma_geral = 0
total_numeros = 0

print("Digite números inteiros positivos (digite 0 para encerrar):")

while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break

    soma_geral += num
    total_numeros += 1

    if num % 2 == 0:
        pares += 1
        soma_pares += num
    else:
        impares += 1

print("\n--- RESULTADOS ---")
print(f"a) Quantidade de pares: {pares} | Quantidade de ímpares: {impares}")

if pares > 0:
    print(f"b) Média dos valores pares: {soma_pares / pares:.2f}")
else:
    print("b) Média dos valores pares: N/A (nenhum par digitado)")

if total_numeros > 0:
    print(f"c) Média geral dos números lidos: {soma_geral / total_numeros:.2f}")
else:
    print("c) NENHUM número válido foi lido.")