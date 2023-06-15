import random

vetor = [0] * 50

for i in range(50):
    vetor[i] = random.randint(0, 20)

print("Vetor: ", vetor)

maior_valor = max(vetor)
print("Maior valor: ", maior_valor)

menor_valor = min(vetor)
print("Menor valor: ", menor_valor)

media_valores = sum(vetor) / len(vetor)
print("Média dos valores: ", media_valores)

qtd_pares = 0
for valor in vetor:
    if valor % 2 == 0:
        qtd_pares += 1
print("Quantidade de valores pares: ", qtd_pares)