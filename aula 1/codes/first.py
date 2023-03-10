## user input in a var and print on consle 
name = input("qual o seu nome? ")
print("Ola, " + name)
## user input bith date and print age
birth = input("qual o seu ano de nascimento? ")
age = 2022 - int(birth)
print(" sua idade é " + str(age) + " anos")
## iser input cpf and print on console formated
cpf = input("qual o seu cpf? ")
print(name + " seu cpf é " +
cpf[0:3] + "." + 
cpf[3:6] + "." + 
cpf[6:9] + "-" + 
cpf[9:11] + 
" e sua idade é " + str(age) + " anos")

