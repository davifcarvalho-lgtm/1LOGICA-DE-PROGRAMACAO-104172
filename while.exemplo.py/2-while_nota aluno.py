while True:
    nota = float(input("Informe a nota do aluno (0 a 10): "))
    if 0 <= nota <= 10:
        break
    print("Nota inválida! A nota deve estar entre 0 e 10.\n")

print(f"Nota informada pelo usuário: {nota}")