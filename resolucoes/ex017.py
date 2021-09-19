from math import hypot
catetoOposto = float(input('Cateto oposto: '))
catetoAdjacente = float(input('Cateto adjacente: '))
#=========================POR MATEMÁTICA==========================
#hipotenusa = sqrt(pow(catetoAdjacente, 2) + pow(catetoOposto, 2))

#=========================PELO MÓDULO==========================
hipotenusa = hypot(catetoOposto, catetoAdjacente)

print(f'A hipotenusa é {hipotenusa:.2f}')