print('Wybierz stopnie w jakich chesz podać zamienianą temperaturę:')
print('1. Stopnie Celsjusza: C')
print('2. Stopnie Fahrenheita: F')
answer = input('Dokonaj wyboru: ')

if answer.upper() == 'C':
    try:
        celsius = float(input('Podaj temperaturę w stopniach Celsjusza: '))
    except ValueError:
        print('Podano niewłaściwą wartość temperatury.')
    else:
        print('Twoja temperatura w stopniach Celsjusza: ', celsius)
        fahrenheit = (celsius * (9 / 5) + 32)
        print('Twoja temperatura w stopniach Fahrenheita: ', fahrenheit)
elif answer.upper() == 'F':
    try:
        fahrenheit = float(input('Podaj temperaturę w stopniach Fahrenheita: '))
    except ValueError:
        print('Podano niewłaściwą wartość temperatury.')
    else:
        print('Twoja temperatura w stopniach Fahrenheita:', fahrenheit)
        celsius = ((fahrenheit - 32) * (5 / 9))
        print('Twoja temperatura w stopniach Celsjusza:', celsius)
else:
    print('Wybrano niewłaściwą opcję. ')