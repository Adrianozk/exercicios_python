lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        opcao = str(input('Deseja continuar(S ou N)? ')).upper()
        if opcao == 'S' or opcao == 'N':
            break
    if opcao == 'N':
        break
print(f'Foram digitados {len(lista)} valores')
print(f'Lista em forma decrescente {sorted(lista, reverse=True)}')
if 5 in lista:
    print('\nO valor 5 está na lista')
else:
    print('\nO valor 5 NÃO está na lista')