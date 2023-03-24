## calcular o aumento de um funcionario, se ganha mais 1500 aumentar 10% se ganha menos aumentar 15%

paycheck = float(input("Digite o valor do seu salario: "))
if paycheck > 1500:
    paycheck = paycheck * 1.1
else:
    paycheck = paycheck * 1.15
print("Seu novo salario é: ", paycheck)