import datetime

days = ['poniedzialek', 'wtorek', 'środa', 'czwartek', 'piatek', 'sobota', 'niedziela']
weekday = datetime.datetime.today().weekday()
print(f'Dzisiaj jest {days[weekday]}.')
