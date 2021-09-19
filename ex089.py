from time import sleep
alunos = []
while True:
    aluno = [str(input('Nome: ')), float(input('1ª nota: ')), float(input('2ª nota: '))]
    alunos.append(aluno)
    while True:
        opcao = str(input('Deseja continuar(S ou N)? ')).upper()
        if opcao == 'S' or opcao == 'N':
            break
    if opcao == 'N':
        break
print('-='*50)
print(F'{"No. NOME":<15}MÉDIA')
print('-'*20)
for i in range(0, len(alunos)):
    print(f'{i:<4}{alunos[i][0]:<10}{(alunos[i][1] + alunos[i][2]) / 2:>6.1f}')

while True:
    print('=' * 47)
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        print('FINALIZANDO...')
        sleep(1)
        print('<<< VOLTE SEMPRE >>>')
        break
    if opcao >= 0 and opcao <= len(alunos):
        print(f'As notas de {alunos[opcao][0]} são {alunos[opcao][1]:.1f} e {alunos[opcao][2]:.1f}')

# =============================== ↓ SOLUÇÃO DO PROFESSOR ↓ =======================

# ficha = list()
# while True:
#     nome = str(input('Nome: '))
#     nota1 = float(input('Nota 1: '))
#     nota2 = float(input('Nota 2: '))
#     media = (nota1 + nota2) / 2
#     ficha.append([nome, [nota1, nota2], media])
#     resp = str(input('Quer continuar? [S/N] '))
#     if resp in 'Nn':
#         break
# print('-=' * 30)
# print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
# print('-' * 26)
# for i, aluno in enumerate(ficha):
#     print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
# while True:
#     print('-' * 35)
#     opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
#     if opc == 999:
#         print('FINALIZANDO...')
#         break
#     if opc <= len(ficha) - 1:
#         print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
# print('<<< VOLTE SEMPRE >>>')