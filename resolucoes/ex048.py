# Calcule a soma entre todos os números impares que são multiplos de 3 e entre 1 e 500
soma = 0
cont = 0
for i in range(1, 501):
    if (i % 2) != 0 and (i % 3) == 0:
        cont += 1
        print(f'{cont}º: {i}')
        soma += i

print(f'Soma de todos os número ímpares entre 1 e 500 é {soma}')