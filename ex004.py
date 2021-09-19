x = input('Digite algo:')
tipoDado = ''
tipoStr = ''
if x.isalnum():
    if x.isnumeric():
        tipoDado = 'numérico'
    if x.isalpha():
        tipoDado = 'alfabético'
        if x.islower():
            tipoStr = 'só caracteres minúsculos'
        if x.isupper():
            tipoStr = 'só caracteres maiúsculos'
        if not x.islower() and not x.isupper():
            tipoStr = 'tanto maúsculos quanto minúsculos'
    elif not x.isnumeric():
        tipoDado = 'alfanumérico'

if tipoStr != '':
    print('O que foi digitado é {} e tem {}'.format(tipoDado, tipoStr))
else:
    print('O que foi digitado é', tipoDado)