import os

idades = []
salarios = []
mulheres_salario_alto = 0

while True:
    print("--- MENU DA PESQUISA ---")
    print("1 | Adicionar pessoa")
    print("2 | Exibir resultados")
    print("3 | Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- CADASTRAR PESSOA ---")
        idade = int(input("Idade: "))
        
        while True:
            sexo = input("Sexo (M/F): ").strip().upper()
            if sexo in ['M', 'F']:
                break
            print("Sexo inválido! Digite M ou F.")
            
        salario = float(input("Salário (R$): "))

        idades.append(idade)
        salarios.append(salario)

        if sexo == 'F' and salario >= 5000.00:
            mulheres_salario_alto += 1

        os.system('cls' if os.name == 'nt' else 'clear')

    elif opcao == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- RESULTADOS DA PESQUISA ---")
        if len(idades) > 0:
            media_salario = sum(salarios) / len(salarios)
            print(f"a) Média de salário do grupo: R$ {media_salario:.2f}")
            print(f"b) Maior idade: {max(idades)} anos | Menor idade: {min(idades)} anos")
            print(f"c) Mulheres com salário >= R$ 5.000,00: {mulheres_salario_alto}\n")
        else:
            print("Nenhuma pessoa cadastrada ainda.\n")

    elif opcao == '3':
        print("\nEncerrando a pesquisa...")
        break
    else:
        print("\nOpção inválida! Tente novamente.\n")