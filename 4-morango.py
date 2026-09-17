morangos = float(input("Quantos Kg de morangos? "))
macas = float(input("Quantos Kg de maçãs? "))

# Preço dos morangos
match morangos:
    case x if x <= 5:
        preco_morango = morangos * 2.50
    case _:
        preco_morango = morangos * 2.20

# Preço das maçãs
match macas:
    case x if x <= 5:
        preco_maca = macas * 1.80
    case _:
        preco_maca = macas * 1.50

total_kg = morangos + macas
total = preco_morango + preco_maca

# Desconto
match total_kg >= 10 or total > 15:
    case True:
        total = total * 0.90
    case False:
        pass

print("Valor a pagar: R$", round(total, 2))