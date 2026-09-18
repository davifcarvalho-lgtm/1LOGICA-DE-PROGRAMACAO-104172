nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

match media:
    case x if x >= 6:
        print("Parabéns! Você foi aprovado!")
    case x if x >= 4:
        print("Você está em recuperação!")
    case _:
        print("Você foi reprovado!")

print("Média:", media)