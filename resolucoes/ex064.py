# leia vários números inteiros pelo teclado.
# o programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# no final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag)
c = 0
soma = 0
numero = 0
while numero != 999:
    numero = int(input('Número inteiro: '))
    if numero != 999:
        c += 1
        soma += numero
print(f'Foram digitados {c} números e a soma deles é {soma}')