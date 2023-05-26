#matriz 3 x 3 com valores de 1 a nome, print com print, um for e dois for 

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=' ')
    print()
