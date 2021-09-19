from math import sin, cos, tan, radians
angulo = int(input('Entre com um angulo qualquer: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'SENO: {seno:.2f}')
print(f'COSSENO: {cosseno:.2f}')
print(f'TANGENTE: {tangente:.2f}')