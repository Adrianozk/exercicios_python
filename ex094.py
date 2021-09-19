pessoa = dict()
listaPessoas = list()
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo(M ou F): ')).upper()
        if sexo == 'F' or sexo == 'M':
            break
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    listaPessoas.append(pessoa.copy())
    pessoa.clear()
    while True:
        opcao = str(input('Deseja continuar(S ou N)? ')).upper()
        if opcao == 'S' or opcao == 'N':
            break
    if opcao == 'N':
        break
somaIdade = 0
for pessoa in listaPessoas:
    somaIdade += pessoa['idade']
mediaIdade = somaIdade / len(listaPessoas)
print(f'\n → Foram cadastradas {len(listaPessoas)} pessoas.')
print(f' → A média de idade é de {mediaIdade:.2f} anos.')
print(f' → As mulheres cadastradas foram ', end='')
for pessoa in listaPessoas:
    if pessoa['sexo'] == 'F':
        print(f'{pessoa["nome"]} ', end='')
print()
print(f' → Lista das pessoas que estão acima da média: ', end='')
for pessoa in listaPessoas:
    if pessoa['idade'] > mediaIdade:
        print('\n')
        for k, v in pessoa.items():
            print(f'{k}: {v}', end='; ')
print('\n<< ENCERRADO >>')