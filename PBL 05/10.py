vetor = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]

for i in range(len(vetor)):
    if vetor.count(vetor[i]) > 1:
        print(vetor[i])
        break
    else:
        continue
