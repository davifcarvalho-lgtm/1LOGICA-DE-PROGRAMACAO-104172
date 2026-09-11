import os
os.system ('cls')

sexo=input("vocé é homem (F) ou mulher (M): ").upper()
altura=float(input("qual a sua altura: "))

match sexo:
    case "M":
        peso= (72.7 * altura) - 58
        print(f"seu peso ideal é: {peso:.2f}kg")

    case "F":
        peso = (61.1 * altura) - 44.7 
        print( f"se peso ideal é: {peso:.2f}kg")
    case _:
        print("sexo invalido")


