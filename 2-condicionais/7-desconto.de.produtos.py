nome = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade: "))
preco = float(input("Digite o preço unitário: "))

total = quantidade * preco

match quantidade:
    case x if x <= 5:
        desconto = total * 0.02
    case x if x <= 10:
        desconto = total * 0.03
    case _:
        desconto = total * 0.05

total_pagar = total - desconto

print("\n--- RESULTADO ---")
print("Produto:", nome)
print("Total: R$", total)
print("Desconto: R$", desconto)
print("Total a pagar: R$", total_pagar)