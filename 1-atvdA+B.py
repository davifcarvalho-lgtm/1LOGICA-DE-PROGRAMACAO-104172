A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

soma = A + B

match soma:
    case x if x < C:
        print("A soma de A + B é menor que C")
    case x if x > C:
        print("A soma de A + B é maior que C")
    case _:
        print("A soma de A + B é igual a C")