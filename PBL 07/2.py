# Escreva um programa que peça ao usuário três números e os armazene em uma
# lista. Em seguida, imprima a lista na tela.

numbers = []

for i in range(3):
    numbers.append(int(input('Digite um número: ')))

print(numbers)