print('-=' * 25)
print(f'{"APROVEITAMENTO DE JOGADORES DE FUTEBOL":^50}')
print('-=' * 25)
jogador = {}
jogadores = []
gols = []
total = cod = 0
while True:
    jogador['cod'] = cod
    jogador['nome'] = str(input('Nome: '))
    qtdPartidas = int(input('Quantas partidas ele jogou? '))
    for partida in range(0, qtdPartidas):
        gols.append(int(input(f'Quantos de gols no {partida + 1}º jogo? ')))
        total += gols[partida]
    jogador['gols'] = gols[:]
    jogador['total'] = total
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    cod += 1
    while True:
        opcao = str(input('Deseja continuar(S ou N)? ')).upper()
        if opcao == 'S' or opcao == 'N':
            break
    if opcao == 'N':
        break
# for jogador in jogadores:
#     print()
#     for k, v in jogador.items():
#         print(f'{k}: {v}')
print('-=' * 30)
print(f'{"cod":<4}{"nome":<15}{"gols":<20}{"total":<5}')
print('-' * 44)
for jogador in jogadores:
    print(f'{str(jogador["cod"]):^3} {str(jogador["nome"]):<15}{str(jogador["gols"]):<20}{str(jogador["total"]):<5}')
while True:
    levantamento = int(input('Mostrar dados de qual jogador? '))
    if levantamento == 999:
        break
    if levantamento >= 0 and levantamento < len(jogadores):
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[levantamento]["nome"]}: ')
        for i, partida in enumerate(jogadores[levantamento]['gols']):
            print(f'    → Na {i + 1}ª partida , fez {partida} gols.')
        print('-' * 44)
    else:
        print(f'ERRO! Não existe jogador com código {levantamento}! Tente novamente')
print('<< VOLTE SEMPRE >>')