import os

dia=int (input("Digite um numero de (1 a 7): "))
match dia:
    case 1:
        print("Domingo final de semana")
    case 2:
        print("Segunda feira dia util")
    case 3:
        print("Terça feira dia util")
    case 4:
        print("Quarta feira dia util")
    case 5:
        print("Quinta feira dia util")
    case 6:
        print("sexta feira dia util")
    case 7:
        print("Sabado final de semana")
    case _:
        print("dia invalido")
print("=== FIM ===")                        