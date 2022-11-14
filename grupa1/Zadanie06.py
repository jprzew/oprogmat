import math

radius = float(input('Podaj długość promienia okręgu: '))

print(f'Długość okręgu: {2*math.pi*radius:.2f} \n'
      f'Pole koła ograniczonego przez okrąg: {math.pi*radius**2:.2f}')
