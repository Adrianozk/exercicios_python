# Leia 2 notas de um aluno e calcule a sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:

# Média abaixo de 5.0 Reprovado
# Média entre de 5.0 e 6.9 Recuperação
# Média 7.0 ou superior Aprovado
nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('REPROVADO!!!')
elif media < 7:
    print('RECUPERAÇÃO!!')
else:
    print('APROVADO!')