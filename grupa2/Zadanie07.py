choice = input('Wybierz: \n'
               '1. Jeśli podajesz temperature w stopniach Celsjusza, \n'
               '2. Jeśli podajesz w stopniach Fahrenheita: \n'
               'Twoj wybor: ')

if choice == '1':
    celsius = float(input('Podaj temperaturę w stopniach Celsjusza: '))
    fahrenheit = celsius * (9 / 5) + 32
    print(f'Twoja temperatura w stopniach fahrenheita: {fahrenheit}')
elif choice == '2':
    fahrenheit = float(input('Podaj temperaturę w stopniach fahrenheita: '))
    celsius = (fahrenheit - 32) * 5/9
    print(f'Twoja temperatura w stopniach Celsjusza: {celsius}')
else:
    print('Wybrano niepoprawną opcję. ')
