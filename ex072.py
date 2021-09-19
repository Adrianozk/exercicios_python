contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
            'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
            'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Entre com um número de 0 a 20: '))
    if numero >= 0 and numero <= 20:
        break
    print('Digite novamente:')
print(f'Você digitou o número {contagem[numero]}')