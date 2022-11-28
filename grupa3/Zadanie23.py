from datetime import datetime


def read_date(text):
    """Reads date from stdin in format dd:mm:YYYY.
       Exits if value given by the user is inappropriate
    """
    answer = input(text)

    try:
        date = datetime.strptime(answer, '%d:%m:%Y').date()
        return date
    except ValueError:
        print('Wpisano niewłaściwą datę. ')
        exit(-1)


date1 = read_date('Podaj datę w formacie dd:mm:rrrr \t')
date2 = read_date('Podaj drugą datę w formacie dd:mm:rrrr \t')

print(f'Liczba dni pomiędzy datami: {abs((date2 - date1).days)}')
