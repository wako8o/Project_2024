items_prices = input().split('|')
budget = float(input())

ticket_price = 150
total_budget = budget
max_price = {'Clothes': 50, 'Shoes': 35.00, 'Accessories': 20.50}

items = [items.split('->') for items in items_prices]
items = [(item[0], float(item[1])) for item in items]
filtrar_price = [price for index, price in items if price <= max_price[index]]

profit = 0
total_price = []
for price in filtrar_price:
    if total_budget >= price:
        total_budget -= price

        total_price = price * 1.4
        total_price.__add__(total_price)

        profit += total_price - price
        print(f'{total_price:.2f}', end=' ')
print()
print(f'Profit: {profit:.2f}')
if budget + profit >= ticket_price:
    print('Hello, France!')
else:
    print('Not enough money.')
