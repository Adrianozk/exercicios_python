# Refaça o desafio 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando o laço for
numero = int(input('Número da tábuada: '))
for i in range(1, 11):
    print(f'{numero} x {i:>2} = {numero * i}')