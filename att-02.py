print('Bem vindo a Lanchonete do Luiggi Abdiel F. S. Santos')
print('***************Cardápio***************')

print('| Código |      Descrição         | Valor |')
print('|   100  |    Cachorro Quente     |  9,00 |')
print('|   101  | Cachorro Quente Duplo  | 11,00 |')
print('|   102  |          X-Egg         | 12,00 |')
print('|   103  |         X-Salada       | 12,00 |')
print('|   104  |         X-Bacon        | 14,00 |')
print('|   105  |          X-Tudo        | 17,00 |')
print('|   200  |   Refrigerante Lata    |  5,00 |')
print('|   201  |        Chá Gelado      |  4,00 |')

total_cost = 0
continue_order = 1

while continue_order:
    product_code = int(input('Entre com o código desejado: '))

    while product_code not in [100, 101, 102, 103, 104, 105, 200, 201]:
        print('Código inválido.')
        product_code = int(input('Entre com o código desejado: '))

    if product_code == 100:
        print('Você pediu um Cachorro Quente no valor de R$9,00')
        total_cost += 9.00

    elif product_code == 101:
        print('Você pediu um Cachorro Quente Duplo no valor de R$11,00')
        total_cost += 11.00

    elif product_code == 102:
        print('Você pediu um X-Egg no valor de R$12,00')
        total_cost += 12.00

    elif product_code == 103:
        print('Você pediu um X-Salada no valor de R$12,00')
        total_cost += 12.00

    elif product_code == 104:
        print('Você pediu um X-Bacon no valor de R$14,00')
        total_cost += 14.00

    elif product_code == 105:
        print('Você pediu um X-Tudo no valor de R$17,00')
        total_cost += 17.00

    elif product_code == 200:
        print('Você pediu um Refrigerante Lata no valor de R$5,00')
        total_cost += 5.00

    elif product_code == 201:
        print('Você pediu um Chá Gelado no valor de R$4,00')
        total_cost += 4.00

    continue_order = int(input('Deseja pedir mais alguma coisa? (1 - Sim, 0 - Não): '))

print('O total a ser pago é R$ {:.2f}'.format(total_cost))
