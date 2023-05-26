part_list = []
part_code = 0


def register_part(code):
    print('Código da Peça: {}'.format(code))

    part_name = input('Entre com o NOME da peça: ')
    part_manufacturer = input('Entre com o FABRICANTE da peça: ')
    part_price = int(input('Entre com o VALOR(R$) da peça: '))

    part_dict = {'code': code, 'name': part_name, 'manufacturer': part_manufacturer, 'price': part_price}

    part_list.append(part_dict.copy())


def search_part():
   while True:
       search_option = input('\nEscolha a opção desejada:\n' +
                               '1 - Consultar TODAS as peças\n' +
                               '2 - Consultar peças por CÓDIGO\n' +
                               '3 - Consultar peças por FABRICANTE\n' +
                               '4 - Retornar\n' +
                               '>> ')

       if search_option == '1':
           print('--------------------')
           for part in part_list:
               for key, value in part.items():
                   print('{}: {}'.format(key, value))
           print('--------------------')
       elif search_option == '2':
           desired_code = int(input('Digite o CÓDIGO da Peça: '))

           for part in part_list:
               if part['code'] == desired_code:
                   print('--------------------')
                   for key, value in part.items():
                       print('{}: {}'.format(key, value))
                   print('--------------------')
       elif search_option == '3':
           desired_code = input('Digite o FABRICANTE da Peça: ')

           for part in part_list:
               if part['manufacturer'] == desired_code:
                   print('--------------------')
                   for key, value in part.items():
                       print('{}: {}'.format(key, value))
                   print('--------------------')
       elif search_option == '4':
           return
       else:
           print('Opção inválida. Tente novamente!')


def remove_part():
    desired_code = int(input('Digite o código da peça a ser removida: '))

    for part in part_list:
        if part['code'] == desired_code:
            part_list.remove(part)
            print('Produto removido')


# Main
print('Bem vindo ao Controle de Estoque da Bicicletaria do Luiggi Abdiel F. S. Santos')
while True:
    main_option = input('\nEscolha a opção desejada:\n' +
                                '1 - Cadastrar Peça(s)\n' +
                                '2 - Consultar Peça(s)\n' +
                                '3 - Remover Peça(s)\n' +
                                '4 - Sair\n' +
                                '>> ')

    if main_option == '1':
        print('Você selecionou a opção Cadastrar Peça')

        part_code += 1
        register_part(part_code)
    elif main_option == '2':
        print('Você selecionou a opção Consultar Peça')

        search_part()
    elif main_option == '3':
        print('Você selecionou a opção de Remover Peça')

        remove_part()
    elif main_option == '4':
        break
    else:
        print('Opção inválida. Tente novamente!')
