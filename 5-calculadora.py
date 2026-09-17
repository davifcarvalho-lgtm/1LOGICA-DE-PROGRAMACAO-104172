operacao = input("Digite a operação (+, -, * ou /): ")

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

match operacao:
    case "+":
        resultado = A + B
    case "-":
        resultado = A - B
    case "*":
        resultado = A * B
    case "/":
        if B != 0:
            resultado = A / B
        else:
            resultado = "Não é possível dividir por zero"
    case _:
        resultado = "Operação inválida"

print("Resultado:", resultado)