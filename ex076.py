produtos = ('Caneta', 1.2, 'Cartolina', 1.0, 'Lápis', 1.0, 'Apontador', 3.5, 'Borracha', 2.0, 'Caderno', 15.9, 'Estojo', 4.9)
print('-' * 30)
print(F'{"LISTAGEM DE PREÇOS":^30}')
print('-' * 30)
for indice, item in enumerate(produtos):
    if indice % 2 == 0:
        print(f'{item:.<20}', end='')
    else:
        print(f'R${item:>6.2f}')
print('-' * 30)