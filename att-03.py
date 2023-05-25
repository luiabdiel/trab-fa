def object_dimensions():
    while True:
        try:
            length = float(input('Digite o comprimento do objeto (em cm): '))
            width = float(input('Digite a largura do objeto (em cm): '))
            height = float(input('Digite a altura do objeto (em cm): '))

            volume = length * width * height

            print('O volume do objeto é (em cm³): {}'.format(volume))

            if volume < 1000:
                return 10
            elif 1000 <= volume < 10000:
                return 20
            elif 10000 <= volume < 30000:
                return 30
            elif 30000 <= volume < 100000:
                return 50
            else:
                print('Não aceitamos objetos com dimensões tão grandes')
                print('Entre com as dimensões desejadas novamente')
                continue

        except ValueError:
            print('Você digitou alguma dimensão do objeto com valor não númerico')
            print('Por favor, entre com as dimensões desejadas novamente')
            continue


def object_weight():
    while True:
        try:
            weight = float(input('Digite o peso do objeto em (kg): '))

            if weight <= 0.1:
                return 1
            elif 0.1 <= weight < 1:
                return 1.5
            elif 1 <= weight < 10:
                return 2
            elif 10 <= weight < 30:
                return 3
            else:
                print('Não aceitamos objetos tão pesados.')
                print('Entre com o peso desejado novamente')

        except ValueError:
            print('Você digitou o peso do objeto com o valor não numérico')
            print('Por favor, entre com o peso desejado novamente')


def route():
    while True:
        route = input('Selecione a rota:\nBR - De Brasilia para Rio de Janeiro\nBS - De Brasilia para São Paulo\nRB - De Rio de Janeiro para Brasilia\nRS - De Rio de Janeiro para São Paulo\nSR - De São Paulo para Rio de Janeiro\nSB - De São Paulo para Brasilia\n>> ')

        route = route.upper()

        if route == 'BR':
            return 1.5
        elif route == 'BS':
            return 1.2
        elif route == 'RB':
            return 1.5
        elif route == 'RS':
            return 1
        elif route == 'SR':
            return 1
        elif route == 'SB':
            return 1.2
        else:
            print('Você digitou uma rota que não existe')
            print('Por favor, entre com a rota desejada novamente')


print('Bem vindo a Companhia de Logística Luiggi Abdiel F. S. Santos')
dimensions = object_dimensions()
object_weight = object_weight()
trip = route()
total = dimensions * object_weight * trip

print('Total a pagar(R$): {:.2f} (dimensões: {:.0f} * peso: {:.0f} * rota: {:.1f})'.format(total, dimensions, object_weight, trip))