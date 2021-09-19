matriz = [[int(input('1º valor: ')),
           int(input('2º valor: ')),
           int(input('3º valor: '))],
          [int(input('4º valor: ')),
           int(input('5º valor: ')),
           int(input('6º valor: '))],
          [int(input('7º valor: ')),
           int(input('8º valor: ')),
           int(input('9º valor: '))]]
for i in range(0, len(matriz)):
        print(f'  [{matriz[i][0]:^3}] [{matriz[i][1]:^3}] [{matriz[i][2]:^3}]')

# =============================== ↓ SOLUÇÃO DO PROFESSOR ↓ =======================

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#     print()