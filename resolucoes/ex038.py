# Leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:

# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
n1 = int(input('1º Numero: '))
n2 = int(input('2º Numero: '))
if n1 == n2:
    input('Não existe valor maior, os dois são iguais.')
elif n1 > n2:
    input('O primeiro valor é maior')
else:
    input('O segundo valor é maior')