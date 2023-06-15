from random import randint

player1 = []
player2 = []

for i in range(3):
    player1.append(randint(1, 6))
    player2.append(randint(1, 6))

if player1 > player2:
    print('Jogador 1 venceu!')
elif player2 > player1:
    print('Jogador 2 venceu!')
else:
    print('Empate!')

print('Jogador 1:', player1)
print('Jogador 2:', player2)
