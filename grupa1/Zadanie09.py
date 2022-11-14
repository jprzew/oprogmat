money = int(input('podaj kwote: '))
amounts = {'200': 0, '100': 0, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0, '1': 0}

for value in amounts:
    amounts[value] = money // int(value)
    money = money % int(value)

print('Aby zrealizować tę kwotę potrzebujesz: ')

for value in amounts:
    if value in ['1', '2', '5']:
        print(amounts[value], f'monet {value}zł')
    else:
        print(amounts[value], f'banknotów {value}zł')
