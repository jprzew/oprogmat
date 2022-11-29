from datetime import datetime


def read_date(text):
    """Reads date from stdin in format %d:%m:%Y. Exits on ValueError"""
    answer = input(text)
    try:
        return datetime.strptime(answer, '%d:%m:%Y').date()
    except ValueError:
        print('Podano niewłaściwą wartość')
        exit(1)


date1 = read_date('Podaj pierwszą datę w formacie dd:mm:rrrr \t')
date2 = read_date('Podaj datę drugą w formacie dd:mm:rrrr \t')

print(f'Różnica dni pomiędzy datami: {abs((date2 - date1).days)}')
