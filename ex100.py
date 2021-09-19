from random import randint
from time import sleep
def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        numero = randint(1, 10)
        print(f'{numero} ', end='')
        numeros.append(numero)
        sleep(0.4)
    print('PRONTO!')
def somaPar():
    print(f'Somando os valores pares de {numeros}, ', end='')
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    print(f'temos {soma}')


numeros = []
sorteia()
somaPar()