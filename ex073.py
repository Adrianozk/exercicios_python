campeonato = ('Athletico-PR', 'Atlético', 'Avaí', 'Bahia', 'Botafogo',
              'CSA', 'Ceará SC', 'Chapecoense', 'Corinthians', 'Cruzeiro', 'Flamengo',
              'FLuminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras', 'Santos', 'São Paulo', 'Vasco da Gama')
print('=-=' * 10)

print('5 primeiros colocados: ')

print('=-=' * 10)
for c in range(0, 5):
    print(f'{c + 1}º {campeonato[c]}')

print('=-=' * 10)

print('Últimos 4 colocados: ')

print('=-=' * 10)
for c in range(16, 20):
    print(f'{c + 1}º {campeonato[c]}')
lista = sorted(campeonato)

print('=-=' * 10)

print('Times em ordem alfabética: ')

print('=-=' * 10)

for time in lista:
    print(f'{time}')

print('=-=' * 10)

print(f'O Chapecoense está na {campeonato.index("Chapecoense")}º posição'
      f'')

print('=-=' * 10)