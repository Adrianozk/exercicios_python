lista = []
while True:
    numero = int(input('Digite um número: '))
    if numero in lista:
        print('Esse número já existe na lista, não será adicionado...')
    else:
        lista.append(numero)
        print('Número adicionado com sucesso!')
    while True:
        opcao = str(input('Deseja continuar(S ou N)? ')).upper()
        if opcao == 'S' or opcao == 'N':
            break
    if opcao == 'N':
        break
lista = sorted(lista)
for item in lista:
    print(item, end='...')