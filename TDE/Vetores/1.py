# Exercício: Ler um vetor de 10 posições e contar quantos valores pares ele possui.
# criando um vetor com o tamanho desejado
vetor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# inicializando a variável contador
contador = 0

# contando a quantidade de elementos pares no vetor
for i in range(10):
  if vetor[i] % 2 == 0:
    contador += 1

# imprimindo a quantidade de elementos pares no vetor
print(contador)