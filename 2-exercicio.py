import os
os.system('cls')
print('os pratos disponiveis no cardapio são: ')
print('codigo    prato              valor')
print('  1   -   picanha        -   25,00')
print('  2   -   lasanha         -  20,00')
print('  3   -   stogonoff      -   18,00')
print('  4   -   bife acebolado -   15,00')
print('  5   -   pão com ovo    -   5,00')



codigo=int(input('Digite um dos codigos no cardapio para solicitar os pratos: '))
match codigo:
    case 1:
        print("picanha")
    case 2:
        print("lasanha")
    case 3:
        print("strogoff")
    case 4:
        print("Bife acebolado")
    case 5:
        print("Pão com ovo")
    
print("=== FIM ===")