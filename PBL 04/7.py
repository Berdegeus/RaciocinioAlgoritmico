vetor = [0] * 15
for i in range(15):
    vetor[i] = int(input(f"Digite o valor da posição {i}: "))
i = 0
while i < len(vetor):
    if vetor[i] == 0:
        for j in range(i, len(vetor) - 1):
            vetor[j] = vetor[j+1]
        vetor[-1] = 0
    else:
        i += 1
print("Vetor compactado: ", end="")
for i in range(len(vetor)):
    if vetor[i] != 0:
        print(vetor[i], end=" ")
print()