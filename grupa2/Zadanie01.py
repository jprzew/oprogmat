try:
    celsius = float(input('Podaj temperaturę w stopniach Celsjusza: '))
except ValueError:
    print('Podano niewłaściwą wartość temperatury.')
else:
    fahrenheit = celsius * (9/5) + 32
    print(f'Twoja temperatura w stopniach Fahrenheita: {fahrenheit:.3f}')
