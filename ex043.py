# Leia o peso e altura e calcule o IMC:

# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida
print('=' * 12)
print('Calculo IMC')
print('=' * 12)
peso = float(input('Peso(Kg): '))
altura = float(input('Altura(m): '))
imc = peso / altura ** 2
print(f'Seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Você tem o peso ideal')
elif imc < 30:
    print('Você sofre de Sobrepeso')
elif imc < 40:
    print('Você sofre de Obesidade')
else:
    print('Você sofre de Obesidade mórbida')