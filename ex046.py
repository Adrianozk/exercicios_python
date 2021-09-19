# Mostre una tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pause de 1 segundo entre eles.
import emoji
from time import sleep
print('Inicio da contagem de fogos de artifício: ')
for i in range(10, -1, -1):
    sleep(1)
    print(f'{i}', '.' * i)
print(emoji.emojize(':fireworks:   ' * 10, True))