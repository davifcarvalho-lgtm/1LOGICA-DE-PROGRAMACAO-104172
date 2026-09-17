litros = float(input("Digite os litros: "))
tipo = input("Digite A para álcool ou G para gasolina: ").upper()

match tipo:
    case "A":
        preco = 3.79

        if litros <= 25:
            desconto = 0.10
        else:
            desconto = 0.20

    case "G":
        preco = 6.59

        if litros <= 25:
            desconto = 0.15
        else:
            desconto = 0.30

    case _:
        preco = 0
        desconto = 0
        print("Combustível inválido")

total = litros * preco
total = total - (total * desconto)

if preco > 0:
    print("Valor a pagar: R$", round(total, 2))