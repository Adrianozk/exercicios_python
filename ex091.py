from random import randint
from time import sleep
from collections import OrderedDict
jogo = {}
print('Valores sorteados: ')
jogo['jogador_1'] = randint(1, 6)
print(f'O jogador_1 tirou {jogo["jogador_1"]}')
sleep(1)
jogo['jogador_2'] = randint(1, 6)
print(f'O jogador_2 tirou {jogo["jogador_2"]}')
sleep(1)
jogo['jogador_3'] = randint(1, 6)
print(f'O jogador_3 tirou {jogo["jogador_3"]}')
sleep(1)
jogo['jogador_4'] = randint(1, 6)
print(f'O jogador_4 tirou {jogo["jogador_4"]}')
jogo = OrderedDict(sorted(jogo.items(), key=lambda kv: kv[1], reverse=True))
print('Ranking dos Jogadores: ')
i = 0
for k, v in jogo.items():
    i += 1
    print(f'{i}º Lugar: {k} com {v}')
    sleep(1)

# ======================= ↓ SOLUÇÃO DO PROFESSOR ↓ =====================

