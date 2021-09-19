#Leia o primeiro termo e a razão de uma PA. no final mostre os 10 primeiros termos da progressão
termo1 = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
decimo = termo1 + (10 - 1) * razao
for c in range(termo1, decimo + razao, razao):
    print(f'{c}', end=' →')
print('\nACABOU')