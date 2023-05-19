# Escreva um programa que crie uma lista com números aleatórios e a imprima na
# tela

from random import randint

numbers = []

for i in range(10):
    numbers.append(randint(1, 100))

print(numbers)
