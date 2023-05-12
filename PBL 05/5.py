pares = 0
impares = 0

for i in range(10):
    numero = int(input("digite um numero inteiro"))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print("numero de pares é", pares)
print("numero de impares é", impares)