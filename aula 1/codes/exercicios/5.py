## input
from datetime import date
BirthDay = int(input("Seu ano de nascimento: "))
BirthMonth = int(input("Seu mes de nascimento: "))
BirthYear = int(input("Seu dia de nascimento: "))
## process
today = date.today()
#calcula sua idade
age = today.year - BirthDay
#se voce ainda nao fez aniversario esse ano, diminui 1 ano. essa logica de if else foi aprendida na aula da rafa segunda :)
if today.month < BirthMonth:
    age -= 1
elif today.month == BirthMonth and today.day < BirthYear:
    age -= 1
#mesma logica de cima, mas para meses
months = today.month - BirthMonth
if today.day < BirthYear:
    months -= 1
if months < 0:
    months += 12
## output
print("Voce tem:", age , "anos e,", months, "meses de idade")

## aqui eu importei a data e hora com  o modulo datetime, voce fazer o mesmo manuamente, mas seu codigo vai acabar desatualizado
## se voce quiser fazer assim, so tirar o from datetime import date e colocar o ano e mes manualmente

