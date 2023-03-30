##print the multiplication table of a insert number

number = int(input('digite um numero'))

for i in range(1, 11):
    print('{} x {} = {}'.format(number, i, number * i))

