money = int(input('Wprowadź kwotę: '))
amounts = {'200': 0, '100': 0, '50': 0, '20': 0,
           '10': 0, '5': 0, '2': 0, '1': 0}

for amount in amounts:
    amounts[amount] = money // int(amount)
    money %= int(amount)

print('Do zrealizowania tej kwoty będziesz potrzebować: ')

for amount in amounts:
    if amount in ['1', '2', '5']:
        print(f'{amounts[amount]} monet {amount} zł')
    else:
        print(f'{amounts[amount]} banknotów {amount} zł')




