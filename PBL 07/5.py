# Escreva um programa que crie uma lista de palavras e imprima a palavra mais
# longa e a palavra mais curta da lista.

words = ['casa', 'carro', 'bicicleta', 'moto', 'ônibus', 'avião', 'barco', 'trem']

print('Palavra mais longa: ', max(words, key=len))
print('Palavra mais curta: ', min(words, key=len))
