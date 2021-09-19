# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
nome = input('Nome completo: ')
if 'SILVA' in nome.upper():
    print('Você tem Silva no nome!')
else:
    print('Você NÃO tem Silva no nome!')