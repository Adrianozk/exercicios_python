cont = soma = 0
while True:
    numero = int(input('Número inteiro: '))
    if numero == 999:
        break
    cont += 1
    soma += numero
print(f'Foram digitados {cont} números e a soma entre eles foi {soma}')