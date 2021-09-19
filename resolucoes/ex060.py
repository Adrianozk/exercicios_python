# leia um número qualquer e mostre seu fatorial
numero = int(input('Número inteiro qualquer: '))
c = numero
fatorial = numero
while c >= 2:
    c -= 1
    fatorial = fatorial * c
print(f'Fatorial de {numero} é {fatorial}')