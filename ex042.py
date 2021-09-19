# Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:

# Equilátero: Todos os lados iguais
# Isósceles: Dois lados iguais
# Escaleno: Todos diferentes
reta1 = float(input('1ª Reta: '))
reta2 = float(input('2ª Reta: '))
reta3 = float(input('3ª Reta: '))
pode = False
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    pode = True
    if reta1 == reta2 and reta2 == reta3:
        print('Essas retas formam um triângulo Equilátero!')
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print('Essas retas formam um triângulo Isósceles!')
    else:
        print('Essas retas formam um triângulo Escaleno!')
else:
    print('Essas retas NÃO podem formar um triângulo!')