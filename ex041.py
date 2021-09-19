# A confederação nacional de natação precisa de um programa que leia
# a data de nascimento de um atleta e mostre sua categoria de acordo com a idade:

# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 20 anos: Sênior
# Acima: Master
from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('Você está na categoria Mirim')
elif idade <= 14:
    print('Você está na categoria Infantil')
elif idade <= 19:
    print('Você está na categoria Junior')
elif idade <= 20:
    print('Você está na categoria Sênior')
else:
    print('Você está na categoria Master')