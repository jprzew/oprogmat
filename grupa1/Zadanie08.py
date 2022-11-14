answer = input('Podaj numer dnia tygodnia: ')
days = {
    '1': 'poniedzialek',
    '2': 'wtorek',
    '3': 'środa',
    '4': 'czwartek',
    '5': 'piatek',
    '6': 'sobota',
    '7': 'niedziela'
}

try:
    print(f'Nazwa dnia tygodnia: {days[answer]}')
except KeyError:
    print('Podano niewłaściwą odpowiedź.')
