total_familias = 0
soma_salarios = 0.0
soma_filhos = 0
maior_salario = None
menor_salario = None

while True:
    print("--- PESQUISA DA PREFEITURA ---")
    print("1 | Adicionar família")
    print("2 | Sair e exibir resultados")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        salario = float(input("Informe o salário da família (R$): "))
        filhos = int(input("Informe o número de filhos: "))

        total_familias += 1
        soma_salarios += salario
        soma_filhos += filhos

        if maior_salario is None or salario > maior_salario:
            maior_salario = salario
        if menor_salario is None or salario < menor_salario:
            menor_salario = salario

        print("\nFamília cadastrada com sucesso!\n")

    elif opcao == '2':
        print("\n=== RESULTADOS FINAIS ===")
        if total_familias > 0:
            print(f"a) Total de famílias pesquisadas: {total_familias}")
            print(f"b) Média salarial da população: R$ {soma_salarios / total_familias:.2f}")
            print(f"c) Média do número de filhos: {soma_filhos / total_familias:.1f}")
            print(f"d) Maior salário: R$ {maior_salario:.2f}")
            print(f"e) Menor salário: R$ {menor_salario:.2f}")
        else:
            print("Nenhuma família foi cadastrada.")
        break
    else:
        print("\nOpção inválida! Tente novamente.\n")