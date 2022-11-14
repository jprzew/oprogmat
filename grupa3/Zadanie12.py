string = input('Podaj ciąg znaków: ')

words = string.split(' ')
words = [word[::-1] for word in words]

print(f'Twój ciąg znaków po odwróceniu: {" ".join(words)}')
