# Leia vários números inteiros pelo teclado.
# no final da execução, mostre a média entre todos os valores lidos.
# o programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
opcao = 'S'
c = 0
soma = 0
while opcao == 'S':
    c += 1
    numero = int(input(f'{c}º número inteiro: '))
    opcao = input('Deseja continuar digitando valores?(S para sim) ').upper()
    soma += numero
print(f'A média entre todos os valores é {soma / c}')