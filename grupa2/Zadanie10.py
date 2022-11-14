# numbers = list(range(1, 101))
# print('Liczby parzyste z przedziału [1, 100]: ')
# print(numbers[1::2])

# for i in range(2, 101, 2):
#     print(i)

bank_notes = [200, 100, 50, 20, 10, 5, 2, 1]
for value in bank_notes:
    if value >= 10:
        print(f'Wartość {value} to banknot.')
    else:
        print(f'Wartość {value}, to moneta.')


