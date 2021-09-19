#Leia 6 números inteiros e mostre a soma apenas daqueles que forem pares
# se for impar desconsidere
soma = 0
for i in range(1, 7):
    numero = int(input(f'{i}º Número inteiro: '))
    if (numero % 2) == 0:
        soma += numero
print(f'A soma de todos os números pares lidos {soma}')