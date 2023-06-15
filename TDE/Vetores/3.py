# Exercicio: Ler 10 inteiros e armazená-los em um vetor. Imprimir o vetor, o maior elemento e sua posição.

# Criando um vetor com tamanho 10, iniciando todos os elementos com 0
vetor = [0] * 10

# Lendo cada número inteiro e salvando na posição correspondente do vetor
for i in range(10):
    vetor[i] = int(input())

# Encontra o maior elemento do vetor e sua posição
maior = vetor[0]
pos = 0
for i in range(1, 10):
    if vetor[i] > maior:
        maior = vetor[i]
        pos = i

# Imprime o vetor, o maior elemento e sua posição
print(vetor)
print(maior)
print(pos)