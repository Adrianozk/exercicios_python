# Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais termos.
# O programa encerra quando ele disser que quer mostrar 0 termos
termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
c = 1
opcao = -1
while c <= 10:
    c += 1
    print(f'{termo}', end=' →')
    termo += razao
while opcao != 0:
    opcao = int(input('Deseja mostrar mais termos(0 para não mostrar mais)? Quantidade: '))
    if opcao != 0:
        while c <= opcao + c:
            c += 1
            print(f'{termo}', end=' →')
            termo += razao
print('ACABOU')