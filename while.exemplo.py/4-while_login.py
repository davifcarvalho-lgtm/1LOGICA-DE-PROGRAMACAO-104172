LOGIN_CORRETO = "admin"
SENHA_CORRETA = "1234"

while True:
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")

    if login == LOGIN_CORRETO and senha == SENHA_CORRETA:
        print("\nAcesso concedido! Bem-vindo(a).")
        break
    else:
        print("Login ou senha incorretos. Tente novamente.\n")