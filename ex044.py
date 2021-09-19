# Calcular o valor a ser pago pelo produto, considerando o seu preço normal e
# condição de pagamento:

# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5%
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
preco = float(input('Valor normal: '))
print('Escolha sua opção de pagamento\n'
      '1 > à vista dinheiro/cheque\n'
      '2 > à vista no cartão\n'
      '3 > no cartão parcelado')
opcao = int(input('Opção: '))
if opcao == 1:
    print(f'Valor total a ser pago: R${preco - (preco * 0.1):.2f}')
elif opcao == 2:
    print(f'Valor total a ser pago: R${preco - (preco * 0.05):.2f}')
elif opcao == 3:
    qtdParcelas = int(input('Em quantas vezes? '))
    if qtdParcelas <= 2:
        print(f'Valor total a ser pago: R${preco:.2f}')
    else:
        print(f'Valor total a ser pago: R${preco + (preco * 0.2):.2f}')