# Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
c = 1
while c <= 10:
    c += 1
    print(f'{termo}', end=' →')
    termo += razao
print('ACABOU')