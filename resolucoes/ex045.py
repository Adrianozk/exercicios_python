# Faça o computador jogar jokenpô.
from random import randint
jog = int(input('Escolha pedra papel ou tesoura(1, 2 ou 3): '))
jogStr = ''
comp = randint(1, 3)
compStr = ''
if jog == 1:
    print('Você escolheu pedra.')
    jogStr = 'pedra'
elif jog == 2:
    print('Você escolheu papel.')
    jogStr = 'papel'
elif jog == 3:
    print('Você escolheu tesoura.')
    jogStr = 'tesoura'

if comp == 1:
    print('O computador escolheu pedra.')
    compStr = 'pedra'
elif comp == 2:
    print('O computador escolheu papel.')
    compStr = 'papel'
elif comp == 3:
    print('O computador escolheu tesoura.')
    compStr = 'tesoura'

print(f'{jogStr} VS {compStr}')

if jog == 1:
    if comp == 2:
        print('Papel enrola pedra! Você perdeu!')
    elif comp == 1:
        print('Empate, jogue novamente!!!')
    elif comp == 3:
        print('Pedra quebra tesoura! Você ganhou!!!')
elif jog == 2:
    if comp == 1:
        print('Papel enrola pedra! Você ganhou!!!')
    elif comp == 2:
        print('Empate, jogue novamente!!!')
    elif comp == 3:
        print('Tesoura recorta papel! Você perdeu!')
if jog == 3:
    if comp == 1:
        print('Pedra quebra tesoura! Você perdeu!')
    elif comp == 3:
        print('Empate, jogue novamente!!!')
    elif comp == 2:
        print('Tesoura recorta papel! Você ganhou!!!')