# Mostre na tela todos os números pares que estão no intervalo entre 1 e 50
j = 0
for i in range(1, 51):
    if (i % 2) == 0:
        j += 1
        print(f'{j}º: {i}')
