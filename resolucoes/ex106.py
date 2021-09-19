def escrevaBrancoPreto(txt):
    print('\033[7;30m~' * (len(txt) + 4), end='')
    print('\033[m')
    print(f'\033[7;30m{txt:^{len(txt) + 4}}',end='')
    print('\033[m')
    print('\033[7;30m~' * (len(txt) + 4), end='')
    print('\033[m')

def escrevaPretoCiano(txt):
    print('\033[36m~' * (len(txt) + 4), end='')
    print('\033[m')
    print(f'\033[36m{txt:^{len(txt) + 4}}', end='')
    print('\033[m')
    print('\033[36m~' * (len(txt) + 4), end='')
    print('\033[m')

def escrevaVermelhoBranco(txt):
    print('\033[30;41m~' * (len(txt) + 4), end='')
    print('\033[m')
    print(f'\033[30;41m{txt:^{len(txt) + 4}}', end='')
    print('\033[m')
    print('\033[30;41m~' * (len(txt) + 4), end='')
    print('\033[m')

def escrevaRoxoPreto(txt):
    print('\033[30;45m~' * (len(txt) + 4), end='')
    print('\033[m')
    print(f'\033[30;45m{txt:^{len(txt) + 4}}',end='')
    print('\033[m')
    print('\033[30;45m~' * (len(txt) + 4), end='')
    print('\033[m')


while True:
    escrevaRoxoPreto('SISTEMA DE AJUDA PyHelp')
    opcao = str(input('Função ou Biblioteca > ')).lower()
    if opcao == 'fim':
        escrevaVermelhoBranco('ATÉ LOGO')
        break
    escrevaPretoCiano(f"Acessando o manual do comando '{opcao}'")
    print('\033[7;30m',end='')
    help(opcao)