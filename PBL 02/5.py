#Faça um programa que peça o peso e a altura de uma pessoa e calcule o seu IMC (índice de massa corporal) e informe se ela está abaixo, dentro ou acima do peso.
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('Com o imc igual a {:.2f}, é considerado: '.format(imc))
if imc < 18.5:
    print('Abaixo do peso normal.')
elif imc >= 18.5 and imc <= 24.9:
    print('Peso normal.')
elif imc >= 25 and imc <= 29.9:
    print('Excesso de peso.')
elif imc >= 30 and imc <= 34.9:
    print('Obesidade classe I')
elif imc >= 35 and imc <= 39.9:
    print('Obesidade classe II')
if imc >= 40:
    print('Obesidade classe III')