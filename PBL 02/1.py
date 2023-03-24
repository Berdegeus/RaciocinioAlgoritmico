# Faça um programa que peça um número inteiro e determine se ele é par ou ímpar.

numero = int(input('Digite um numero: '))

if numero % 2 == 0:
    print(f'{numero} é par')
else:
    print(f'{numero} é impar')