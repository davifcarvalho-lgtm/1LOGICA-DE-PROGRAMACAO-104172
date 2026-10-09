# Validação da primeira nota
while True:
    nota1 = float(input("Informe a primeira nota (0 a 10): "))
    if 0 <= nota1 <= 10:
        break
    print("Nota inválida! Tente novamente.\n")

# Validação da segunda nota
while True:
    nota2 = float(input("Informe a segunda nota (0 a 10): "))
    if 0 <= nota2 <= 10:
        break
    print("Nota inválida! Tente novamente.\n")

media = (nota1 + nota2) / 2
print(f"\nMédia aritmética do aluno: {media:.2f}")