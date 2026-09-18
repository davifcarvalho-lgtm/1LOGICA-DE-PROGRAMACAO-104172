renda = float(input("Digite sua renda: "))
emprestimo = float(input("Digite o empréstimo: "))
prestacoes = int(input("Digite as prestações: "))

valor = emprestimo / prestacoes

if emprestimo <= renda * 10 and valor <= renda * 0.30:
    print("Empréstimo aprovado")
else:
    print("Empréstimo negado")