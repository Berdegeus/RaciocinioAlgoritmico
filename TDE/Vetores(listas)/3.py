# Exercício: Ler um vetor de 8 posições, ler dois valores X e Y correspondentes a duas posições do vetor e escrever a soma dos valores encontrados nas respectivas posições X e Y

vetor = []  # cria uma lista vazia
for i in range(8):
    valor = int(input())  # lê um valor do usuário como inteiro
    vetor.append(valor)  # adiciona o valor no final da lista

x, y = map(int, input("Digite os valores de X e Y separados por espaço: ").split())  # lê dois números do usuário separados por espaço e converte para inteiros

if x < 0 or x >= len(vetor) or y < 0 or y >= len(vetor):
    print("Valores de X e Y estão fora do intervalo válido.")
else:
    soma = vetor[x] + vetor[y]  # realiza a soma dos valores nas posições X e Y
    print(soma)  # exibe o resultado da soma
