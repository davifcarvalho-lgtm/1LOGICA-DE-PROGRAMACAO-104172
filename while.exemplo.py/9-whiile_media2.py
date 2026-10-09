soma_notas = 0.0
contador = 0

while True:
    nota = float(input(f"Informe a {contador + 1}ª nota: "))
    soma_notas += nota
    contador += 1

    resposta = input("Deseja inserir mais uma nota? (S/N): ").strip().upper()
    if resposta == 'N':
        break

if contador > 0:
    media = soma_notas / contador
    print(f"\nQuantidade de notas inseridas: {contador}")
    print(f"Média aritmética: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")