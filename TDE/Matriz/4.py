# Exercício: Ler matriz 4x4, imprimir a matriz e retornar a localização (linha e coluna) do maior valor

# Ler a matriz
matriz = []
for i in range(4):
    linha = list(map(int, input().split()))
    matriz.append(linha)

# Encontrar o maior valor e sua posição na matriz
maior_valor = 0
linha_maior_valor = 0
coluna_maior_valor = 0
for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior_valor:
            maior_valor = matriz[i][j]
            linha_maior_valor = i
            coluna_maior_valor = j

# Imprimir a matriz e os valores
for linha in range(4):
    for coluna in range(4):
        print(matriz[linha][coluna], end=" ")
    print()
print(linha_maior_valor, coluna_maior_valor)