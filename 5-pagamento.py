import os
os.system ('cls')
valor=float(input('quanto foi o valor: '))
forma_de_pagamento =input('qual seria a forma de pagamento (V) ou (P): ')
desconto = valor*0.10
valor_final=valor - desconto
prestaçoes1=valor/2
prestaçoes2=valor/3
pestaçoes3=valor/4
prestaçoes4=valor/5
prestaçoes5=valor/6


match forma_de_pagamento :
    case 'V':
        print =("pelo pagamento ser a vista ganhara 10% de desconto saindo por {valor final} ")
    case "P":
        parcela=(input("quantas parcelas o senhor quer pagar? Vamos até 6x: "))
match parcela:
        case 2:
            print(f'sera 2 parcelas de {prestaçoes1}')
        case 3:
            print(f'sera 3 parcelas de {prestaçoes2}')
        case 4:
            print(f'sera 4 parcelas de {prestaçoes3}')
        case 5:
            print(f'sera 5 parcelas de {prestaçoes4}')
        case 6:
            print(f'sera 6 parcelas de {prestaçoes6}')
        case _:
            print('quantidade de parcelas invalidas')


