# from random import randint

# print('bem vindo a loteria')
# print('escolha 6 numeros de 1 a 60')

# sorteio = []

# for i in range(6):
#     sorteio.append(randint(1, 60))

# print(sorteio)

# aposta = []

# for i in range(6):
#     aposta.append(int(escolha('digite um numero: ')))

# print(aposta)

# acertos = 0

# for i in range(6):
#     if aposta[i] in sorteio:
#         acertos += 1

# print('voce acertou', acertos, 'numeros')

# using while loop

from random import randint

print('bem vindo a loteria')
print('escolha 6 numeros de 1 a 60')

sorteio = []

while len(sorteio) < 6:
    num = randint(1, 60)
    if num not in sorteio:
        sorteio.append(num)

escolha = []

while len(escolha) < 6:
    num = int(input('digite um numero: '))
    if num not in escolha:
        escolha.append(num)

acertos = 0

while len(escolha) > 0:
    if escolha[0] in sorteio:
        acertos += 1
    escolha.pop(0)

print('voce acertou', acertos, 'numeros')

