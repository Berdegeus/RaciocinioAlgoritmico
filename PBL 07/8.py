# Escreva um programa que crie uma lista com os números de 1 a 10 elevados ao
# quadrado. Em seguida, calcule a soma dos elementos da lista e imprima o
# resultado.

numbers = []

for i in range(1, 11):
    numbers.append(i ** 2)

print('Soma: ', sum(numbers))


