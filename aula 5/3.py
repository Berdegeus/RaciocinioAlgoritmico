## collect numbers until the user input -1 and print the average of all numbers

number = int(input('digite um numero '))
sum = 0
count = 0

while number != -1:
    sum += number
    count += 1
    number = int(input('digite um numero '))

print('a media é {}'.format(sum / count))



