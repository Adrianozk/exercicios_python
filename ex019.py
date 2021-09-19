from random import randint, choice

# =====================MINHA SOLUÇÃO====================
escolha = randint(0, 3)

aluno1 = input('1º Aluno: ')
aluno2 = input('2º Aluno: ')
aluno3 = input('3º Aluno: ')
aluno4 = input('4º Aluno: ')

# SWITCH CASE
if escolha == 0:
    escolhido = aluno1
elif escolha == 1:
    escolhido = aluno2
elif escolha == 2:
    escolhido = aluno3
elif escolha == 3:
    escolhido = aluno4

print(f'O aluno escolhido para apagar a lousa foi {escolhido}')

# =====================SOLUÇÃO DO PROFESSOR====================
# aluno1 = input('1º Aluno: ')
# aluno2 = input('2º Aluno: ')
# aluno3 = input('3º Aluno: ')
# aluno4 = input('4º Aluno: ')
# lista = [aluno1, aluno2, aluno3, aluno4]
# escolhido = choice(lista)
# print(f'O aluno escolhido para apagar a lousa foi {escolhido}')
