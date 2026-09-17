cor = input("Digite a cor do CD: ").lower()

match cor:
    case "verde":
        preco = 10
    case "azul":
        preco = 20
    case "amarelo":
        preco = 30
    case "vermelho":
        preco = 40
    case _:
        preco = 0
        print("Cor inválida!")

if preco > 0:
    print("O preço do CD é: R$", preco)