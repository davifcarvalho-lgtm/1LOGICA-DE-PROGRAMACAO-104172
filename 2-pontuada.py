nome = input("Digite o nome:")
sexo =input("Digite o sexo (M/F:): ")
estado = input("Digite o estado civil: ")

if sexo.upper() == "F" and estado.upper() == "CASADA":
    tempo = int(input("Digite o tempo de casada em anos: "))
else:
    tempo = 0
print("nome: ", nome)
print("sexo: ", sexo)
print("Estado civil: ", estado)

if sexo.upper() == "F" and estado.upper () == "CASADA"
    print("tempo de casada:", tempo,"anos")