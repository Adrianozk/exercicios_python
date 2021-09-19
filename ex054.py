# leia o ano de nascimento de 7 pessoas. No final
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
# considerando maioridade como 21 anos
from datetime import date
maiores = menores = 0
for i in range(1, 8):
    ano = int(input(f'{i}º Ano de nascimento: '))
    if date.today().year - ano >= 21:
        maiores += 1
    else:
        menores += 1
print(f'{maiores} pessoas atingiram a maioridade\n'
      f'{menores} NÃO atingiram a maioridade')