tupla = (int(input('1º valor: ')),
         int(input('2º valor: ')),
         int(input('3º valor: ')),
         int(input('4º valor: ')))
print(f'Você digitou os valores {tupla}')
print('-=' * 20)
print(f'O número 9 apareceu {tupla.count(9)} vezes')
print('-=' * 20)
if 3 in tupla:
    print(f'O número 3 foi digitado primeiro na {tupla.index(3) + 1}ª posição')
print('O número 3 não foi digitado em nenhuma posição')
print('-='*  20)
print('Os valores pares digitados foram ', end='')
for numero in tupla:
    if numero % 2 == 0:
        print(numero, end=' ')
print()
print('-='*  20)