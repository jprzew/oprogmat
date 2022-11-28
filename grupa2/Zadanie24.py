from sys import argv

if len(argv) > 1:
    argument = argv[1]
    print(argument[::-1])
else:
    print('Nie podano argumentu!')
