vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
vetor_resultado = []
for i in range(10):
    if i % 2 == 0:
        vetor_resultado.append(vetor1[i])
    else:
        vetor_resultado.append(vetor2[i])
print(vetor_resultado)