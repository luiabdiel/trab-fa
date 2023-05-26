list_peca = []
codigo_peca = 0


def cadastrar_peca(codigo):
    print('Código da Peça: {}'.format(codigo))

    nome_peca = input('Entre com o NOME da peça: ')
    fabricante_peca = input('Entre com o FABRICANTE da peça: ')
    preco_peca = int(input('Entre com o VALOR(R$) da peça: '))

    dicionario_peca = {'codigo': codigo,
                       'nome': nome_peca,
                       'fabricante': fabricante_peca,
                       'preco': preco_peca
                       }

    list_peca.append(dicionario_peca.copy())


def consultar_peca():
   while True:
       opcao_consultar = input('\nEscolha a opção desejada:\n' +
                               '1 - Consultar TODAS as peças\n' +
                               '2 - Consultar peças por CÓDIGO\n' +
                               '3 - Consultar peças por FABRICANTE\n' +
                               '4 - Retornar\n' +
                               '>> ')

       if opcao_consultar == '1':
           print('--------------------')
           for peca in list_peca:
               for key, value in peca.items():
                   print('{}: {}'.format(key, value))
           print('--------------------')
       elif opcao_consultar == '2':
           codigo_desejado = int(input('Digite o CÓDIGO da Peça: '))

           for peca in list_peca:
               if peca['codigo'] == codigo_desejado:
                   print('--------------------')
                   for key, value in peca.items():
                       print('{}: {}'.format(key, value))
                   print('--------------------')
       elif opcao_consultar == '3':
           codigo_desejado = input('Digite o FABRICANTE da Peça: ')

           for peca in list_peca:
               if peca['fabricante'] == codigo_desejado:
                   print('--------------------')
                   for key, value in peca.items():
                       print('{}: {}'.format(key, value))
                   print('--------------------')
       elif opcao_consultar == '4':
           return
       else:
           print('Opção inválida. Tente novamente!')


def remover_peca():
    codigo_desejado = int(input('Digite o código da peça a ser removida: '))

    for peca in list_peca:
        if peca['codigo'] == codigo_desejado:
            list_peca.remove(peca)
            print('Produto removido')


# Main
print('Bem vindo ao Controle de Estoque da Bicicletaria do Luiggi Abdiel F. S. Santos')
while True:
    opcao_principal = input('\nEscolha a opção desejada:\n'+
                                '1 - Cadastrar Peça(s)\n'+
                                '2 - Consultar Peça(s)\n'+
                                '3 - Remover Peça(s)\n'+
                                '4 - Sair\n'+
                                '>> ')

    if opcao_principal == '1':
        print('Você selecionou a opção Cadastrar Peça')

        codigo_peca += 1
        cadastrar_peca(codigo_peca)
    elif opcao_principal == '2':
        print('Você selecionou a opção Consultar Peça')

        consultar_peca()
    elif opcao_principal == '3':
        print('Você selecionou a opção de Remover Peça')

        remover_peca()
    elif opcao_principal == '4':
        break
    else:
        print('Opção inválida. Tente novamente!')
