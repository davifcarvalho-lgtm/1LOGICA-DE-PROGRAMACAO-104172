while True:
    print("--- CARDÁPIO / MENU ---")
    print("1 - Café Express: R$ 5.00")
    print("2 - Suco Natural: R$ 8.00")
    print("3 - Salgado: R$ 7.00")
    print("4 - Sanduíche: R$ 12.00")
    print("5 - Sobremesa: R$ 10.00")
    
    opcao = input("Escolha uma opção (1 a 5): ")

    if opcao == '1':
        print("\nOpção escolhida: Café Express | Preço: R$ 5.00")
        break
    elif opcao == '2':
        print("\nOpção escolhida: Suco Natural | Preço: R$ 8.00")
        break
    elif opcao == '3':
        print("\nOpção escolhida: Salgado | Preço: R$ 7.00")
        break
    elif opcao == '4':
        print("\nOpção escolhida: Sanduíche | Preço: R$ 12.00")
        break
    elif opcao == '5':
        print("\nOpção escolhida: Sobremesa | Preço: R$ 10.00")
        break
    else:
        print("\nOpção inválida! Tente novamente.\n")