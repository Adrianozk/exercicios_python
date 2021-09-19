# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.

# Para salários superiores a R$1.250,00 , calcule um aumento de 10%.

# Para os inferiores ou iguais, o aumento é de 15%
salarioAtual = float(input('Salário atual: '))
if salarioAtual > 1250:
    aumento = salarioAtual * 0.1
else:
    aumento = salarioAtual * 0.15
print(f'O salário de R${salarioAtual:.2f} terá um aumento de R${aumento:.2f}\n'
      f'o novo salário será de R${salarioAtual + aumento:.2f}')