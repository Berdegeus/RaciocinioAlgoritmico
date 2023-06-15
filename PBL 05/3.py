valor = int(input('Digite um número inteiro (1 a 10): '))

if valor < 1 or valor > 10:
    print('Valor inválido. Digite um valor entre 1 e 10.')

else:
    for i in range (0, 11):
        resultado = valor * i
        print(f'{valor} x {i} = {resultado}')