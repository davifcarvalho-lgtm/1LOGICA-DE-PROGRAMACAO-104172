import os 
os.system("cls")

#ENTRADA
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

if imc <= 18.5:
    resultado = "abaixo do peso."
elif imc <= 24.9:
    resultado = "peso ideal (parabens)"
elif imc <= 34.9:
    resultado = "Obesidade grau I."
elif imc <= 39.9:
    resultado = "obesidade garu II (severa)"
else:
    resultado = "obesidade grau III (mórbida)"




