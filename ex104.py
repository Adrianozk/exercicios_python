def leiaInt(msg=''):
    while True:
        entrada = str(input(msg))
        if entrada.isnumeric():
            return int(entrada)
        else:
            print(f'\033[1;31mERRO! Digite um número inteiro válido.\033[m')


n = leiaInt('Número inteiro: ')
print(f'Você acabou de digitar o número {n}')