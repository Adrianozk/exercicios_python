# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa.O programa vai perguntar o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal,
# sabendo que ela não pode exceder 30% do salário ou então
# o empréstimo será negado.
valorCasa = float(input('Valor da casa: '))
salarioCompr = float(input('Salário do comprador: '))
tempPag = int(input('Anos para pagar: '))
prestMens = valorCasa / (tempPag * 12)
if prestMens <= salarioCompr * 0.3:
    print(f'Emprestimo aprovado!!!\nSua prestação mensal será de R${prestMens:.2f}')
else:
    print(f'Emprestimo negado.\nSua prestação seria de R${prestMens:.2f}\nMas infelizmente não condiz com seu salário de R${salarioCompr:.2f}')