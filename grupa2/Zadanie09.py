bank_notes = [200, 100, 50, 20, 10, 5, 2, 1]
money = int(input('Wpisz kwotę: '))

for value in bank_notes:
    if money < 10:
        print(f'Liczba monet o nominale {value}: {money // value}')
    else:
        print(f'Liczba banknotów o nominale {value}: {money // value}')
    money %= value


#
#
#
# print(f'Liczba banknotów o nominale 200: {bank_notes // 200}')
# bank_notes %= 200
#
# print(f'Liczba banknotów o nominale 100: {bank_notes // 100}')
# bank_notes %= 100
#
# print(f'Liczba banknotów o nominale 50: {bank_notes // 50}')
# bank_notes %= 50
#
# print(f'Liczba banknotów o nominale 20: {bank_notes // 20}')
# bank_notes %= 20
#
# print(f'Liczba banknotów o nominale 10: {bank_notes // 10}')
# bank_notes %= 10
#
# print(f'Liczba monet o nominale 5: {bank_notes // 5}')
# bank_notes %= 5
#
# print(f'Liczba monet o nominale 2: {bank_notes // 2}')
# bank_notes %= 2
#
# print(f'Liczba monet o nominale 1: {bank_notes}')
