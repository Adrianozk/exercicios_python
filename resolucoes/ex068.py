from random import randint
vitorias = 0
playerNum = -1
playerOp = ''
while True:
    while playerOp != 'P' and playerOp != 'I':
        playerOp = input('Par ou ímpar(P ou I)? ').upper()
    comp = randint(0, 10)
    print(f'comp: {comp}')
    while playerNum < 0 or playerNum > 10:
        playerNum = int(input('Número(0 a 10): '))
    soma = comp + playerNum
    if playerOp == 'P':
        if soma % 2 == 0:
            print('Você ganhou!!!')
            vitorias += 1
            playerNum = -1
            playerOp = ''
        else:
            print('Você perdeu!')
            print(f'Ganhou {vitorias} vezes consecutivas')
            break
    elif playerOp == 'I':
        if soma % 2 == 0:
            print('Você perdeu!')
            print(f'Ganhou {vitorias} vezes consecutivas')
            break
        else:
            print('Você ganhou!!!')
            vitorias += 1
            playerNum = -1
            playerOp = ''