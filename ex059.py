# leia 2 valores e mostre um menu na tela

# 1 somar
# 2 multiplicar
# 3 maior
# 4 novos numeros
# 5 sair do programa

# seu programa deverá realizar a operação solicitada em cada caso
from time import sleep
opcao = 0
while opcao != 5:
    valor1 = float(input('1º Valor: '))
    valor2 = float(input('2º Valor: '))
    print('MENU\n'
          '1 Somar\n'
          '2 Multiplicar\n'
          '3 Maior\n'
          '4 Novos números\n'
          '5 Sair do programa')
    opcao = int(input('Opção:\n'))
    if opcao == 1:
        print(f'{valor1} + {valor2} = {valor1 + valor2}')
    elif opcao == 2:
        print(f'{valor1} x {valor2} = {valor1 * valor2}')
    elif opcao == 3:
        if valor1 == valor2:
            print('Os 2 valores são iguais.')
        elif valor1 > valor2:
            print(f'{valor1} é maior que {valor2}')
        else:
            print(f'{valor2} é maior que {valor1}')