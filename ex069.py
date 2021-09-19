maiores = homens = novinhas = 0
while True:
    sexo = opcao = ''
    idade = int(input('Idade: '))
    while sexo != 'M' and sexo != 'F':
        sexo = input('Sexo(M ou F): ').upper()
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        novinhas += 1
    while opcao != 'S' and opcao != 'N':
        opcao = input('Deseja continuar(S ou N)? ').upper()
    if opcao == 'N':
        print('▓' * 30)
        print(f'Pessoas com mais de 18 anos: {maiores}')
        print(f'Homens cadastrados: {homens}')
        print(f'Mulheres com menos de 20 anos: {novinhas}')
        break