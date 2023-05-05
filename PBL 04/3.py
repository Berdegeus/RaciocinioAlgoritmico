# Faça um programa que preenche um vetor com valores inteiros até que
# o usuário digite um valor negativo (o valor negativo não deve ser
# inserido no vetor)

entrada = []

while True:
    num = int(input('digite um numero: '))
    if num < 0:
        break
    entrada.append(num)

print(entrada)

## quantidade de valores maior que 5

maior = 0 

for i in range(len(entrada)):
    if entrada[i] > 5:
        maior += 1

print('A quantidade de numeros maior que 5 é:', maior)

## soma dos pares

par = 0
impar = 0

for i in range(len(entrada)):
    if entrada[i] % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1


print('par:', par)
print('impar:', impar)

# quantidade de numeros no vetor
print(len(entrada))







