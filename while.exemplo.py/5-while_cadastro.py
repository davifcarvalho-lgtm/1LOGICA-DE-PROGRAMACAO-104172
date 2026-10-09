import os

print("--- CADASTRO ---")
login_cadastrado = input("Crie seu login: ")
senha_cadastrada = input("Crie sua senha: ")

# Limpa o terminal (compatível com Windows, Linux e macOS)
os.system('cls' if os.name == 'nt' else 'clear')

print("--- LOGIN ---")
while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login == login_cadastrado and senha == senha_cadastrada:
        print("\nAcesso permitido!")
        break
    else:
        print("Login ou senha incorretos! Tente novamente.\n")