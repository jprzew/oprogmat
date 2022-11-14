number = int(input('Podaj liczbę w systemie dziesiętnym: '))

result = ''
while number > 0:
  result = str(number % 2) + result
  number //= 2

print(f'Twoja liczba w systemie dwójkowym: {result}')


