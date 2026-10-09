notas = []

for i in range(1, 4):
    while True:
        nota = float(input(f"Informe a {i}ª nota (0 a 10): "))
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        print("Nota inválida! Tente novamente.")

media = sum(notas) / 3
print(f"\nMédia: {media:.2f}")

if media >= 7.0:
    print("Situação: Aprovado")
elif 5.0 <= media <= 6.9:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")