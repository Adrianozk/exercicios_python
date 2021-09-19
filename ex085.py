listaNumeros = [[],[]]
for i in range(0, 7):
    numero = int(input(f'{i + 1}º valor: '))
    if numero % 2 == 0:
        listaNumeros[0].append(numero)
    else:
        listaNumeros[1].append(numero)
listaNumeros[0].sort()
listaNumeros[1].sort()
print(f'Os valores pares digitados foram {listaNumeros[0]}')
print(f'Os valores ímpares digitados foram {listaNumeros[1]}')

# =============== ↓ SOLUÇÃO DO PROFESSOR ↓ ===============

# num = [[], []]
# valor = 0
# for c in range(1, 8):
#     valor = int(input(f'Digite o {c}º valor: '))
#     if valor % 2 == 0:
#         num[0].append(valor)
#     else:
#         num[1].append(valor)
# print('-=' * 30)
# num[0].sort()
# num[1].sort()
# print(f'Os valores pares digitados foram: {num[0]}')
# print(f'Os valores ímpares digitados foram: {num[1]}')