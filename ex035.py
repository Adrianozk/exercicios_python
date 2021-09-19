# Desenvolva um programa que leia o comprimento de três retas
# e figa ao usuário se elas podem ou não formar um triângulo
reta1 = float(input('1ª Reta: '))
reta2 = float(input('2ª Reta: '))
reta3 = float(input('3ª Reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Essas retas podem formar um triângulo')
else:
    print('Essas retas NÃO podem formar um triângulo')