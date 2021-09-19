# Leia o peso de 5 pessoas e mostre qual foi o maior e o menor peso lidos
maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input(f'{i + 1}º Peso(Kg): '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior}Kg')
print(f'O menor peso lido foi {menor}Kg')