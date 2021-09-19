# Escreva um programa que leia a velocidade de um carro

# se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.

# A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = int(input('Velocidade do seu carro: '))
if velocidade > 80:
    multa = 7 * (velocidade - 80)
    print(f'Você foi multado em R${multa:.2f} por estar acima de 80 Km/h.')
else:
    print('Você está digirindo dentro do limite!')