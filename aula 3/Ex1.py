## calculate the elo based on your score
## 0 to 999 iron
## 1000 to 1999 bronze
## 2000 to 2999 silver
## 3000 to 3999 gold
## 4000 to 4999 platinum
## 5000 to 5999 diamond
## 6000 to 6999 master
## 7000 to 7999 grandmaster
## 8000 to 8999 challenger

score = int(input('Seu score: '))


if score < 0:
    print('Como voce conseguiu um elo negativo?')
elif score < 1000:
    print('Seu elo é Iron')
elif score < 2000:
    print('Seu elo é Bronze')
elif score < 3000:
    print('Seu elo é Silver')
elif score < 4000:
    print('Seu elo é Gold')
elif score < 5000:
    print('Seu elo é Platinum')
elif score < 6000:
    print('Seu elo é Diamond')
elif score < 7000:
    print('Seu elo é Master')
elif score < 8000:
    print('Seu elo é Grandmaster')
elif score < 9000:
    print('Seu elo é Challenger')
else:
    print('Entao voce é o Faker?')



