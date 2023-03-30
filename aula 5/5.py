## input numbers and print how many are pair and how many are odd

n = int(input('digite um numero: '))
count = 0
count2 = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        count += 1
    else:
        count2 += 1

print('a quantidade de numeros pares é {} e a quantidade de numeros impares é {}'.format(count, count2))