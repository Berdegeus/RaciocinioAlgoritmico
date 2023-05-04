numeros = [5, 7 , 12, 2, 9, 21]

# for i in range(len(numeros)):
#     print(numeros[i])

print(numeros)
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
print(numeros[4])
print(numeros[5])
print()

numeros[1] = 17
numeros[3] = 22
numeros[2] = 1
numeros[4] = 29
print(numeros)
print()

soma = numeros[5] + numeros[4]
sub = numeros[3] - numeros[1]
mult = numeros[0] * numeros[5]
div = numeros[3] / numeros[2]
print(soma, sub, mult, int(div))
print()

i = 0
while i < len(numeros):
    print(numeros[i])
    i += 1





