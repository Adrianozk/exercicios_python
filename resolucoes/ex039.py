# Leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:

# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo de alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
if idade < 18:
    print('Ainda não é o momento de se alistar.')
    print(f'Falta {18 - idade} ano(s) para o seu alistamento.')
elif idade == 18:
    print('Esta na hora de se alistar!!!')
else:
    print(f'Já passou {idade - 18} ano(s) do seu tempo de alistamento.')