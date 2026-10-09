LOGIN_CORRETO = "aluno"
SENHA_CORRETA = "senai"

tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")

    if login == LOGIN_CORRETO and senha == SENHA_CORRETA:
        print("\nLogin realizado com sucesso!")
        break
    else:
        tentativas += 1
        restantes = max_tentativas - tentativas
        if restantes > 0:
            print(f"Dados incorretos! Você ainda tem {restantes} tentativa(s).\n")
        else:
            print("\nNúmero máximo de tentativas excedido. Programa finalizado.")