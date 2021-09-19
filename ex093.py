print('-=' * 25)
print(f'{"APROVEITAMENTO DE JOGADOR DE FUTEBOL":^50}')
print('-=' * 25)
jogador = {}
gols = []
totalGols = qtdPartidas = 0
jogador['nome'] = str(input('Nome: '))
qtdPartidas = int(input('Quantas partidas ele jogou? '))
for partida in range(0, qtdPartidas):
    gols.append(int(input(f'Quantos de gols no {partida + 1}º jogo? ')))
    totalGols += gols[partida]
jogador['gols'] = gols[:]
jogador['total'] = totalGols
print()
for k, v in jogador.items():
    print(f'{k}: {v}')
print(f'O jogador {jogador["nome"]} jogou {qtdPartidas} partidas.')
for i, partida in enumerate(jogador['gols']):
    print(f'    → Na {i + 1}ª partida , fez {partida} gols.')
print(f'Foi um total de {totalGols} gols.')