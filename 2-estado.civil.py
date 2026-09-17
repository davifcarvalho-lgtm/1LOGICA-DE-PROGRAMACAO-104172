nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ").upper()
estado_civil = input("Digite o estado civil: ").upper()

tempo_casada = 0

match (sexo, estado_civil):
    case ("F", "CASADA"):
        tempo_casada = int(input("Há quantos anos está casada? "))

print("\n--- DADOS DA PESSOA ---")
print("Nome:", nome)
print("Sexo:", sexo)
print("Estado civil:", estado_civil)

if sexo == "F" and estado_civil == "CASADA":
    print("Tempo de casada:", tempo_casada, "anos")