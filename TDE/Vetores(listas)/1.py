# Exercício: Ler 6 valores inteiros e mostrar na tela

# Lendo valores inteiros e armazenando em uma lista
valores = []
for i in range(6):
    valores.append(int(input("Valor: ")))

# Mostrando os valores lidos na tela
for valor in valores:
    print(valor)