# Exercício: Calcular o quadrado das componentes de um vetor

# vetor com os números reais
vetor_real = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# vetor com o quadrado das componentes do vetor_real
vetor_quadrado = []

# itera sobre o vetor_real e calcula o quadrado de cada elemento, adicionando no vetor_quadrado
for numero in vetor_real:
  vetor_quadrado.append(numero ** 2)

# imprime os vetores
print(vetor_real)
print(vetor_quadrado)