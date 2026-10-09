total_pago = 0.0

while True:
    print("\n--- CARDÁPIO ---")
    print("1 - Prato Executivo: R$ 25.00")
    print("2 - Massa Italiana:  R$ 30.00")
    print("3 - Salada Completa: R$ 20.00")
    print("4 - Suco Natural:    R$  8.00")

    opcao = input("Escolha o número do prato desejado: ")

    if opcao == '1':
        total_pago += 25.00
        print("Prato Executivo adicionado!")
    elif opcao == '2':
        total_pago += 30.00
        print("Massa Italiana adicionada!")
    elif opcao == '3':
        total_pago += 20.00
        print("Salada Completa adicionada!")
    elif opcao == '4':
        total_pago += 8.00
        print("Suco Natural adicionado!")
    else:
        print("Opção inválida! Nenhum item adicionado.")

    resposta = input("\nDeseja escolher outro prato? (S/N): ").strip().upper()
    if resposta == 'N':
        break

print(f"\nTotal a ser pago pelo cliente: R$ {total_pago:.2f}")