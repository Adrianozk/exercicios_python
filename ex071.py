valor = int(input('Valor do saque: '))
restante = valor
ced50 = ced20 = ced10 = ced1 = 0
if restante >= 50:
    ced50 = restante // 50
    restante = restante % 50
if restante >= 20:
    ced20 = restante // 20
    restante = restante % 20
if restante >= 10:
    ced10  = restante // 10
    restante = restante % 10
if restante >= 1:
    ced1 = restante // 1
    restante = restante % 1
print(f'\nTotal de {ced50} cédula(s) de 50\n'
      f'Total de {ced20} cédula(s) de 20\n'
      f'Total de {ced10} cédula(s) de 10\n'
      f'Total de {ced1} cédula(s) de 1')