lista = []
c = maiorPeso = menorPeso = 0
while True:
    pessoa = [str(input('Nome: ')), float(input('Peso: '))]
    lista.append(pessoa)
    c += 1
    if c == 1:
        maiorPeso = pessoa[1]
        menorPeso = pessoa[1]
    else:
        if pessoa[1] > maiorPeso:
            maiorPeso = pessoa[1]
        if pessoa[1] < menorPeso:
            menorPeso = pessoa[1]
    while True:
        opcao = str(input('Deseja continuar(S ou N)? ')).upper()
        if opcao == 'S' or opcao == 'N':
            break
    if opcao == 'N':
        break

print(f'Foram cadastradas {c} pessoas')
print(f'Pessoas mais pesadas: ',end='')
for pessoa in lista:
    if pessoa[1] == maiorPeso:
        print(f'[{pessoa[0]}] ', end='')
print(f'\nPessoas mais leves: ', end='')
for pessoa in lista:
    if pessoa[1] == menorPeso:
        print(f'[{pessoa[0]}] ', end='')
print(f'O maior peso foi {maiorPeso:.1f}Kg e o menor foi {menorPeso:.1f}Kg')