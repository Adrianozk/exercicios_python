from time import sleep
def contador(inicio, fim, passo):

    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1

    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(f'{c} ', end='')
            sleep(0.3)
    else:
        for c in range(inicio, fim - 1, - passo):
            print(f'{c} ', end='')
            sleep(0.3)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))