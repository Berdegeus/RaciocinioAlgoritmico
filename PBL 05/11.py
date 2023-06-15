inputA = input("Digite os elementos do vetor A separados por espaço: ")
inputB = input("Digite os elementos do vetor B separados por espaço: ")

vectorA = inputA.split()
vectorB = inputB.split()
vectorC = []

for i in range(len(vectorA)):
    vectorC.append(int(vectorA[i]) + int(vectorB[i]))

print(vectorC)