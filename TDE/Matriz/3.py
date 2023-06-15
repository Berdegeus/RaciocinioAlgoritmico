# Exercício: Criar matriz 4x4 com o valor do produto linha x coluna

# criando a matriz de 4x4 inicialmente com zeros
matriz = [[0 for j in range(4)] for i in range(4)]

# percorrendo a matriz com dois loops encadeados
for i in range(4):
    for j in range(4):
        matriz[i][j] = i*j  # calculando o produto da linha e coluna

# imprimindo a matriz na tela
for linha in matriz:
    print(linha)