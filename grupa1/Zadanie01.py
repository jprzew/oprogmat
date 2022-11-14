try:
    celsius = float(input('Podaj temperaturę w stopniach Celsjusza: '))
except ValueError:
    print('Wpisano niewłaściwą wartość. ')
else:
    fahrenheit = celsius * 1.8 + 32
    print(f'Twoja temperatura w stopniach Fahrenheita: {fahrenheit:.3f}')
