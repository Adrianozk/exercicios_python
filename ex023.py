# Faça um programa que leia um número de 0 9999
# e mostre na tela cada um dos dígitos separados
# Ex:
# Digite um número: 1834

#Unidade: 4
#Dezena: 3
#Centena: 8
#Milhar: 1
# =======================MINHA SOLUÇÃO======================
# numero = input('Digite um número de 0 a 9999: ')
# tamanho = len(numero)
# if tamanho == 4:
#     print(f'Unidade: {numero[3]}\n'
#           f'Dezena: {numero[2]}\n'
#           f'Centena: {numero[1]}\n'
#           f'Milhar: {numero[0]}')
#
# elif tamanho == 3:
#     print(f'Unidade: {numero[2]}\n'
#           f'Dezena: {numero[1]}\n'
#           f'Centena: {numero[0]}')
#
# elif tamanho == 2:
#     print(f'Unidade: {numero[1]}\n'
#           f'Dezena: {numero[0]}')
#
# elif tamanho == 1:
#     print(f'Unidade: {numero}')

# =======================SOLUÇÃO DO PROFESSOR======================
numero = int(input('Digite um número de 0 a 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'Analisando o número {numero}')
print(f'Unidade: {u}\n'
      f'Dezena: {d}\n'
      f'Centena: {c}\n'
      f'Milhar: {m}')