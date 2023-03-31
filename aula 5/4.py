## input a N number and sum all the numbers from 1 to N

n = int(input('digite um numero: '))
sum = 0

for i in range(1, n+1):
    sum += i
print(f('a soma de todos os numeros de 1 ate {n} e {sum}'))


