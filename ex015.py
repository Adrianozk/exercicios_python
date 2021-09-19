diasAlug = int(input('Quantos dias alugados? '))
kmRodados = int(input('Quantos KM rodados? '))
precoAlug = 60 * diasAlug
precoKm = kmRodados * 0.15
precoTotal = precoKm + precoAlug
print(f'O total a pagar é R${precoTotal}')