print('Bem vindo à Loja do Luiggi Abdiel F. S. Santos')

product_price = float(input('Entre com o valor do produto: '))
product_quantity = int(input('Entre com a quantidade do produto: '))

discount_rate = 0

if product_quantity < 10:
    discount_rate = 0.0
elif 10 <= product_quantity <= 99:
    discount_rate = 0.5
elif 100 <= product_quantity <= 999:
    discount_rate = 0.10
elif product_quantity >= 1000:
    discount_rate = 0.15

total_value = product_price * product_quantity
discount_amount = total_value * discount_rate
final_value = total_value - discount_amount

print('O valor sem desconto foi: R$ {:.2f}'.format(total_value))
print('O valor com desconto foi: R$ {:.2f} ({:.0f}% de desconto)'.format(final_value, discount_rate * 100))
