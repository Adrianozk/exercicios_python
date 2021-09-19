from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram {tupla[0]} {tupla[1]} {tupla[2]} {tupla[3]} {tupla[4]}')
maior = 0
menor = 11
for numero in tupla:
    if maior < numero:
        maior = numero
    if menor > numero:
        menor = numero
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')