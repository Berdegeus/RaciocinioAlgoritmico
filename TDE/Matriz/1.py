# Exercício: ler matriz 4x4 e contar valores maiores que 10
matriz = [
    [2, 12, 5, 8],
    [15, 6, 4, 20],
    [7, 9, 14, 3],
    [11, 1, 18, 13]
]

# conta valores maiores que 10
qtd_maiores_10 = 0
for linha in matriz:
    for num in linha:
        if num > 10:
            qtd_maiores_10 += 1

# imprime quantidade
print(qtd_maiores_10)
