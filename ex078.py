lista = [int(input('1º número: ')), int(input('2º número: ')), int(input('3º número: ')), int(input('4º número: ')), int(input('5º número: '))]

maior = [0, 0]
menor = [999999, 0]
for indice, item in enumerate(lista):
    if item > maior[0]:
        maior[0] = item
        maior[1] = indice
    if item < menor[0]:
        menor[0] = item
        menor[1] = indice
print(f'O maior valor foi {maior[0]} na {maior[1] + 1}ª posição')
print(f'O menor valor foi {menor[0]} na {menor[1] + 1}ª posição')