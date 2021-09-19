matriz = [[int(input('1º valor: ')),
           int(input('2º valor: ')),
           int(input('3º valor: '))],
          [int(input('3º valor: ')),
           int(input('4º valor: ')),
           int(input('5º valor: '))],
          [int(input('6º valor: ')),
           int(input('7º valor: ')),
           int(input('8º valor: '))]]
print()
for i in range(0, len(matriz)):
        print(f'  [{matriz[i][0]:^3}] [{matriz[i][1]:^3}] [{matriz[i][2]:^3}]')
somaPar = somaTerc = maiorSeg = 0
for i in range(0, 3):
    somaTerc += matriz[i][2]
    for j in range(0, 3):
        if matriz[i][j] % 2 == 0:
            somaPar += matriz[i][j]
        if matriz[1][j] > maiorSeg:
            maiorSeg = matriz[1][j]

print(f'\nA soma dos valores PARES é {somaPar}')
print(f'A soma dos valores da TERCEIRA COLUNA é {somaTerc}')
print(f'O MAIOR valor da SEGUNDA LINHA é {maiorSeg}')

# =============================== ↓ SOLUÇÃO DO PROFESSOR ↓ =======================

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# spar = mai = scol = 0
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# print('-=' * 15)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#         if matriz[l][c] % 2 == 0:
#             spar += matriz[l][c]
#     print()
# print('-=' * 15)
# print(f'A soma dos valores pares é {spar}')
# for l in range(0, 3):
#     scol += matriz[l][2]
# print(f'A soma dos valores da terceira coluna é {scol}')
# for c in range(0, 3):
#     if c == 0 or matriz[1][c]:
#         mai = matriz[1][c]
# print(f'O maior valor da segunda linha é {mai}')