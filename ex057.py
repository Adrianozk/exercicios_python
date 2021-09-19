# Leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite o sexo(M, F): ').upper()
    if sexo == 'M' or sexo == 'F':
        print(f'Sexo {sexo} salvo com sucesso!')
    else:
        print('Escreva o valor corretamente! M OU F!!!!')