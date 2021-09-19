# leia nome, idade e sexo de 4 pessoas. no final mostre:

# a média de idade do grupo
# nome do homem mais velho
# quantas mulheres tem menos de 20 anos
somaIdades = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totalMulher20 = 0
for i in range(1, 5):
    print('=' * 5, f'{i}ª Pessoa ', '=' * 5)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo(M, F): ').upper()
    somaIdades += idade
    if i == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulher20 += 1

mediaIdade = somaIdades / 4
print(f'A média de idade do grupo é de {mediaIdade} anos')
print(f'O nome do mais velho é o {nomeVelho} com {maiorIdadeHomem} anos')
print(f'Ao todo são {totalMulher20} mulher(es) com menos de 20 anos')