import os 
os.system("cls")

#inicio

media=float(input("digite sua media: "))
faltas=int(input("digite suas faltas: "))

#process

if media<7 and faltas>40:
    resultado= ("reprovado") 
else:  
    resultado= ("aprovado")
print(resultado) 