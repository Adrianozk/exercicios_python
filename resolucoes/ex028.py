# Escreva um programa que faça o computador "pensar" em um número
# inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

# o programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
print('Vou pensar em um número de 0 a 5...')
print('\n\n')
comp = randint(0, 5)
user = int(input('Tente adivinhar o número: '))
if comp == user:
    print(f'Parabéns você acertou!!!\nComputador: {comp}\nVocê: {user}')
else:
    print(f'Infelizmente você errou...\nNão desista! Tente novamente!!!\nComputador: {comp}\nVocê: {user}')