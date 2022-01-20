prices = [57.08, 46.51, 97, 48, 2.45, 11.07, 85, 46.11, 8.06, 64,
          15.1, 55, 16.89, 17.09, 61, 5, 13.87, 39.05, 43.55, 31.95]
# A
for i in prices:
    rub, kop = f'{i:.2f}'.split('.')
    print(f'{rub} руб. {kop} коп.,', end=' ')

# B
print(f'ID base: {id(prices)} - {prices}')
prices.sort()
print(f'ID change: {id(prices)} - {prices}')

# C
list = sorted(prices, reverse=True)
print(f'ID change: {id(list)} - {list}')

# D
print(f'{list[:5][::-1]}')
