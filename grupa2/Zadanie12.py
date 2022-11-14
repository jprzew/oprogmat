string = input('Podaj ciąg znaków: ')

words = string.split(' ')
words = [word[::-1] for word in words]
print(' '.join(words))
