from datetime import datetime


def read_date(text):
    """Reads date in format %d:%m:%Y from stdin.
    Shows error message if date is inappropriate"""

    answer = input(text)
    try:
        date = datetime.strptime(answer, '%d:%m:%Y').date()
        return date
    except ValueError:
        print('Podano niewłaściwą datę!')
        exit(-1)


date1 = read_date('Podaj pierwszą datę w formacie dd:mm:rrrr\t')
date2 = read_date('Podaj drugą datę w formacie dd:mm:rrrr\t')

print(f'Różnica dni pomiędzy datami: {abs((date2 - date1).days)}')



