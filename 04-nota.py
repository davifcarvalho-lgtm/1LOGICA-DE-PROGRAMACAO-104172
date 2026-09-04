import os
os.system("cls")

#inicio

nota=float(input("Digite sua nota: "))
max=10
min=0

if nota>=min and nota<=max:
    mostre=(f"nota:{nota} ")
else:
    mostre=(f"Sua nota {nota} deve estar entre 10 e 0")
print(mostre)
