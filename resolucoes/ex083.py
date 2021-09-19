expressao = str(input('Digite uma expressão: '))
left = expressao.count('(')
right = expressao.count(')')
if left == right:
    print('A expressão é válida')
else:
    print('A expressão está ERRADA')
