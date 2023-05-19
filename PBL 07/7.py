# Escreva um programa que crie uma lista com os números de 1 a 100. Em seguida,
# imprima apenas os números pares da lista.

numbers = []

for i in range(1,101):
    if i % 2 == 0:
        numbers.append(i)

print(numbers)
