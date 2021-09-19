# Faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor
n1 = int(input('1º Número: '))
n2 = int(input('2º Número: '))
n3 = int(input('3º Número: '))
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

print(f'O maior é o {maior} e o menor é {menor}')