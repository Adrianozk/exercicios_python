# melhore o jogo desafio 028 onde o computador vai pensar em um número entre 0 e 10
# Só que agora o jogador vai tentar adivinhar até ele acertar,
# mostrando no final quantos palpites foram necessários para vencer
from random import randint
comp = randint(0, 11)
player = -1
print('O computador pensou em um número entre 0 e 10')
while player != comp:
    player = int(input('Tente adivinhar qual foi: '))
    if player != comp:
        print('Você errou. Tente novamente!!')
print('\nParabéns você acertou!!!')