print('Wybierz konwersję: ')
print('1. Stopnie Celsjusza na Fahrenheita.')
print('2. Stopnie Fahrenheita na Celsjusza.')
option = input('Wybierz opcję: ')

if option == '1':
    celsius = float(input('Podaj temperature w stopniach Celcjusza: '))
    fahrenheit = celsius * 1.8 + 32
    print('Twoja temperatura w stopniach Fahrenheita: ', round(fahrenheit, 2))

elif option == '2':
    fahrenheit = float(input('Podaj temperature w stopniach Fahrenheita: '))
    celsius = (fahrenheit - 32) / 1.8
    print('Twoja temperatura w stopniach Celcjusza: ', round(celsius, 2))
else:
    print('Podano mi złą wartość')
