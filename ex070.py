total = barato = c = caro = 0
nomeBarato = ''
while True:
    c += 1
    nome = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    total += preco
    opcao = ''
    if preco > 1000:
        caro += 1
    if c == 1:
        barato = preco
        nomeBarato = nome
    elif preco < barato:
        barato = preco
        nomeBarato = nome
    while opcao != 'S' and opcao != 'N':
        opcao = input('Deseja continuar comprando(S ou N)? ').upper()
    if opcao == 'N':
        break
print(f'\nNo total foi gasto R${total:.2f}')
print(f'{caro} produtos custam mais de R$1000.00')
print(f'O produto mais barato foi {nomeBarato} custando R${barato:.2f}')