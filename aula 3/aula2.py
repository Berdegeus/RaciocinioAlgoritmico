## calculate the medium of 4 numbers if more then 7  you pass bettween 4 and 7 final exam and less then 4 you fail

# input
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
n3 = float(input('digite a terceira nota: '))
n4 = float(input('digite a quarta nota: '))

# process
media = (n1 + n2 + n3 + n4) / 4

# output
if media >= 7:
    print('voce passou com media: ', media)

elif media >= 4 and media < 7:
    print('voce esta de recuperaçao com media: ', media)

else:
    print('voce nao passou com media: ', media)

