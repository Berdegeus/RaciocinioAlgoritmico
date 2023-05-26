## Jogo da velha em python utilizando matriz 3x3

matriz = [[' ',' ',' '] for i in range(3)]

def JogoDaVelha():
    print('Jogo da velha')
    print('Jogador 1: X')
    print('Jogador 2: O')
    print('Para jogar, digite a linha e a coluna que deseja jogar')
    print('Linha: 0, 1 ou 2')
    print('Coluna: 0, 1 ou 2')
    print('Exemplo: 0 1')
    print()
    print('  0 1 2')
    for i in range(3):
        print(i, end=' ')
        for j in range(3):
            print(matriz[i][j], end=' ')
        print()
    print()

def jogada(jogador):
    print('Jogador', jogador)
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    if jogador == 1 and matriz[linha][coluna] == ' ':
        matriz[linha][coluna] = 'X'
    elif jogador == 2 and matriz[linha][coluna] == ' ':
        matriz[linha][coluna] = 'O'
    else:
        print('Jogada inválida')
        jogada(jogador)
    print()
    print('  0 1 2')
    for i in range(3):
        print(i, end=' ')
        for j in range(3):
            print(matriz[i][j], end=' ')
        print()
    print()

def vencedor():
    vencedor = 0
    for i in range(3):
        #linhas
        if matriz[i][0] == matriz[i][1] == matriz[i][2] == 'X':
            vencedor = 1
        if matriz[i][0] == matriz[i][1] == matriz[i][2] == 'O':
            vencedor = 2
        if matriz[0][i] == matriz[1][i] == matriz[2][i] == 'X':
            vencedor = 1
        if matriz[0][i] == matriz[1][i] == matriz[2][i] == 'O':
            vencedor = 2
        #diagonais
        if matriz[0][0] == matriz[1][1] == matriz[2][2] == 'X':
          vencedor = 1
        if matriz[0][0] == matriz[1][1] == matriz[2][2] == 'O':
          vencedor = 2
        if matriz[0][2] == matriz[1][1] == matriz[2][0] == 'X':
          vencedor = 1
        if matriz[0][2] == matriz[1][1] == matriz[2][0] == 'O':
          vencedor = 2
    return vencedor

def main():
    JogoDaVelha()
    jogador = 1
    while vencedor() == 0:
        jogada(jogador)
        if jogador == 1:
            jogador = 2
        else:
            jogador = 1
    print('Jogador', vencedor(), 'venceu!')

main()