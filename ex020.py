# O mesmo professor do ex019 quer sortear a ordem de apresentação dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
from random import randint, shuffle

# =====================MINHA SOLUÇÃO====================

aluno1 = input('1º Aluno: ')
aluno2 = input('2º Aluno: ')
aluno3 = input('3º Aluno: ')
aluno4 = input('4º Aluno: ')

primeiro = randint(0, 3)
while True:
    segundo = randint(0, 3)
    if segundo != primeiro:
        break
while True:
    terceiro = randint(0, 3)
    if terceiro != primeiro and terceiro != segundo:
        break
while True:
    quarto = randint(0, 3)
    if quarto != primeiro and quarto != segundo and quarto != terceiro:
        break

def escolheAluno(aluno):
    if aluno == 0:
        escolhido = aluno1
    elif aluno == 1:
        escolhido = aluno2
    elif aluno == 2:
        escolhido = aluno3
    elif aluno == 3:
        escolhido = aluno4
    return escolhido

print('Primeiro: ', escolheAluno(primeiro))
print('Segundo: ', escolheAluno(segundo))
print('Tercero: ', escolheAluno(terceiro))
print('Quarto: ', escolheAluno(quarto))

# =====================SOLUÇÃO DO PROFESSOR====================
# aluno1 = input('1º Aluno: ')
# aluno2 = input('2º Aluno: ')
# aluno3 = input('3º Aluno: ')
# aluno4 = input('4º Aluno: ')
# lista = [aluno1, aluno2, aluno3, aluno4]
# shuffle(lista)
# print('A ordem de apresentação será: ')
# print('Primeiro: ', lista[0])
# print('Segundo: ', lista[1])
# print('Tercero: ', lista[2])
# print('Quarto: ', lista[3])