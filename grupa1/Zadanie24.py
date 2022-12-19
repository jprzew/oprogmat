from sys import argv

try:
    string = argv[1]
except IndexError:
    print('Podaj więcej parametrów.')
else:
    print(string[::-1])
