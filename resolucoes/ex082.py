lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        opcao = str(input('Deseja continuar(S ou N)? ')).upper()
        if opcao == 'S' or opcao == 'N':
            break
    if opcao == 'N':
        break
for item in lista:
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)
print(f'Lista original: {lista}')
print(f'Pares: {pares}')
print(f'impares: {impares}')