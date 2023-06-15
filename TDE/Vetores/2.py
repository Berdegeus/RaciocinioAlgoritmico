# Exercício: Receber vetor do usuário e imprimir o maior e o menor elemento

# Recebendo um vetor de tamanho 10 do usuário e armazenando na variável 'vetor'
vetor = [int(input("Numero: ")) for i in range(10)]

# Armazenando o primeiro elemento do vetor nas variáveis 'maior' e 'menor'
maior = vetor[0]
menor = vetor[0]

# Percorrendo todo o vetor e atualizando as variáveis 'maior' e 'menor'
for i in range(1, len(vetor)):
    if vetor[i] > maior:
        maior = vetor[i]
    elif vetor[i] < menor:
        menor = vetor[i]

# Imprimindo o maior e o menor elemento do vetor
print(maior, menor)