n = int(input("Digite o número de idades: "))
soma = 0

for i in range(n):
    idade = int(input("Digite a idade: "))
    soma += idade

media = soma / n

print("A média das idades é:", media)