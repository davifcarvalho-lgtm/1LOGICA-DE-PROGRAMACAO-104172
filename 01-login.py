import os 
os.system("cls")

login= input("digite seu login: ")
senha= input("digite sua senha: ")

login_salvo = "Davi"
senha_salva = "123@"

login_esta_coreto = login == login_salvo
senha_esta_correta = senha == senha_salva 

if login and senha_esta_correta:
    print("bem vindo! ")
else:
    print("login ou senha invalidos ")
    