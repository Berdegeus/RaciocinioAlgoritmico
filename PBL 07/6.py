# Escreva um programa que crie duas listas, uma com os números pares de 1 a 10
# e outra com os números ímpares de 1 a 10. Em seguida, junte as duas listas em
# uma terceira lista e a imprima na tela.

even = []
odd = []

for i in range(1,11):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

odd.extend(even)
odd.sort()

print(odd)




