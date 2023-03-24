## ask user age and if 18 years old or more, show you can have a license

#input
age = int(input('quantos anos voce tem? '))

#process and output
if age >= 18:
    print('com essa idade voce pode tirar a carteira de motorista')
else: 
    print('com essa idade voce nao pode tirar a carteira de motorista')
