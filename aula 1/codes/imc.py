##calculate imc limit 2 numbers after comma
weight = float(input("qual o seu peso? "))
height = float(input("qual a sua altura? "))
imc = weight / (height * height)
print("seu imc é " + str(round(imc, 2)))