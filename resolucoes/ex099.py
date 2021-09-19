from time import sleep
def maior(* lista):
    print('-=' * 30)
    print('Analisando os valores passados...')

    maior = 0

    for i, numero in enumerate(lista):
        print(f'{numero} ', end='')
        if i == 0:
            maior = numero
        if numero > maior:
            maior = numero
        sleep(0.3)
    sleep(0.7)
    print(f'Foram informados {len(lista)} valores ao todo.')
    sleep(1)
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()