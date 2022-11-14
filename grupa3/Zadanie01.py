try:
    celsius = float(input('Podaj temperature w stopniach Celsjusza: '))
except ValueError:
    print('Podano niewłaściwą wartość temperatury.')
else:
    fahrenheit = 1.8 * celsius + 32
    print(f'Twoja temperatura w stopniach Fahrenheita: {fahrenheit:.3f}')
