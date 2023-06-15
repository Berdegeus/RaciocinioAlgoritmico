# Exercício: Criar matriz 5x5 e preencher com 1 na diagonal principal e 0 nos demais elementos.

# Iniciando matriz 5x5 com valores iguais a 0
matriz = [[0 for j in range(5)] for i in range(5)]

# Preenchendo diagonal principal com valores iguais a 1
for i in range(5):
  matriz[i][i] = 1

# Imprimindo matriz
for linha in matriz:
  print(linha)