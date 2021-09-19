while True:
    numero = int(input('Qual tabuada deseja? (0 pra sair) '))
    if numero == 0:
        break
    for i in range(1, 11):
        print(f'{numero} x {i:>2} = {numero * i}')