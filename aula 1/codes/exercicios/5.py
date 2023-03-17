## input
from datetime import date
birth_year = int(input("Seu ano de nascimento: "))
birth_month = int(input("Seu mes de nascimento: "))
birth_day = int(input("Seu dia de nascimento: "))
## process
today = date.today()
#calcula sua idade
age = today.year - birth_year
#se voce ainda nao fez aniversario esse ano, diminui 1 ano. essa logica de if else foi aprendida na aula da rafa segunda :)
if today.month < birth_month:
    age -= 1
elif today.month == birth_month and today.day < birth_day:
    age -= 1
#mesma logica de cima, mas para meses
months = today.month - birth_month
if today.day < birth_day:
    months -= 1
if months < 0:
    months += 12
## output
print("Voce tem:", age , "anos e,", months, "meses de idade")

## aqui eu importei a data e hora com  o modulo datetime, voce fazer o mesmo manuamente, mas seu codigo vai acabar desatualizado
## se voce quiser fazer assim, so tirar o from datetime import date e colocar o ano e mes manualmente

