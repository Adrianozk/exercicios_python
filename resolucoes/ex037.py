# Leia um número inteiro qualquer e peça para o usuário escolher qual
# será a base de conversão:

# 1 para binário
# 2 para octal
# 3 para hexadecimal
numero = int(input('Número inteiro qualquer: '))
base = int(input('Escolha uma base de conversão:\n'
                 '1 Binário\n'
                 '2 Octal\n'
                 '3 Hexadecimal\n'))
if base == 1:
    print(f'Binário: {bin(numero)}')
elif base == 2:
    print(f'Octal: {oct(numero)}')
elif base == 3:
    print(f'Hexadecimal: {hex(numero)}')