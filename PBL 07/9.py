# Escreva um programa que crie uma lista com as letras do alfabeto e embaralhe
# suas posições. Em seguida, peça ao usuário para adivinhar a posição correta de
# uma determinada letra e informe se ele acertou ou errou.

import random

alphabet = list('abcdefghijklmnopqrstuvwxyz')

random.shuffle(alphabet)

letter = input('Digite uma letra: ')
position = int(input('Digite a posição da letra: '))
position -= 1

if alphabet[position] == letter:
    print('Você acertou!')
else:
    print('Você errou!')



