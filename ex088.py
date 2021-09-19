from random import randint
from time import sleep
print('-' * 30)
print(f'{"JOGUE NA MEGA SENA":^30}')
print('-' * 30)
qtdJogos = int(input('Quantos jogos deseja sortear? '))
print(f'{f" SORTEANDO {qtdJogos} JOGOS ":-^35}')
jogos = []
for i in range(0, qtdJogos):
    jogo = []
    for j in range(0, 6):
        numero = randint(1, 60)
        while numero in jogo:
            numero = randint(1, 60)
        jogo.append(numero)
    jogos.append(sorted(jogo))
    sleep(1)
    print(f'Jogo {i + 1}: {jogos[i]}')
print(f'{" BOA SORTE! ":$^35}')

# =============================== ↓ SOLUÇÃO DO PROFESSOR ↓ =======================

# from random import randint
# from time import sleep
# lista = list()
# jogos = list()
# print('-' * 30)
# print(f'{"JOGA NA MEDA SENA":^30}')
# print('-' * 30)
# quant = int(input('Quantos você quer que eu sorteie? '))
# totalJogos = 1
# while totalJogos <= quant:
#     cont = 0
#     while True:
#         num = randint(1, 60)
#         if num not in lista:
#             lista.append(num)
#             cont += 1
#         if cont >= 6:
#             break
#     lista.sort()
#     jogos.append(lista[:])
#     lista.clear()
#     totalJogos += 1
# print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
# for i, l in enumerate(jogos):
#     print(f'Jogo {i + 1}: {l}')
#     sleep(1)
# print('-=' * 5, '< BOA SORTE! >', '-=' * 5)