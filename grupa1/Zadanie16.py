def kelvin(temperature, input_scale):
    """Converts temperature to kelvins"""

    if input_scale == 'c':
        return temperature + 273.15
    elif input_scale == 'f':
        return (temperature + 459.67) * 5 / 9
    else:
        return None


def celsius(temperature, input_scale):
    """Converts temperature to Celsius degrees"""

    if input_scale == 'k':
        return temperature - 273.15
    elif input_scale == 'f':
        return (temperature - 32) / 1.8000
    else:
        return None


def fahrenheit(temperature, input_scale):
    """Converts temperature to Fahrenheit degrees"""

    if input_scale == 'c':
        return temperature * 9 / 5 + 32
    elif input_scale == 'k':
        return (temperature - 273.15) * 1.8000 + 32
    else:
        return None


conversions = {'k': kelvin, 'c': celsius, 'f': fahrenheit}
scale_names = {'k': 'Kelwina', 'c': 'Celsjusza', 'f': 'Fahrenheita'}


while True:
    input_scale = input('Wybierz skalę, w której podasz temperaturę. Wpisz k - jeśli to skala Kelvina,\n'
                        ' f - jeśli skala Fahrenheita, c - jeśli skala Celsjusza: ')

    if input_scale in {'f', 'c', 'k'}:
        break

    print('Podano niewłaściwą opcję\n')

while True:
    try:
        temperature = float(input('Podaj temperaturę: '))
        break
    except ValueError:
        print('Podano niewłąściwą wartość temperatury! \n')


while True:
    output_scale = input('Wybierz skalę, w której chcesz otrzymać wybraną temperaturę. '
                         'Wpisz k - jeśli to skala Kelvina,\n'
                         ' f - jeśli skala Fahrenheita, c - jeśli skala Celsjusza: ')

    if output_scale in {'f', 'c', 'k'}:
        break

    print('Podano niewłaściwą opcję\n')

print(f'Twoja temperatura w skali {scale_names[output_scale]} '
      f'wynosi: {conversions[output_scale](temperature, input_scale)}')
