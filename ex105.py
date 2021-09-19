def notas(* n, situacao=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n:  uma ou mais notas dos alunos (aceita várias)
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    turma = {}
    turma['qtdNotas'] = len(n)
    turma['maior'] = -1
    turma['menor'] = 11
    somaNotas = 0
    for nota in n:
        somaNotas += nota
        if nota > turma['maior']:
            turma['maior'] = nota
        if nota < turma['menor']:
            turma['menor'] = nota
    turma['media'] = somaNotas / len(n)
    if situacao:
        if turma['media'] > 7:
            turma['situacao'] = 'Boa'
        elif turma['media'] >= 5:
            turma['situacao'] = 'Razoavel'
        else:
            turma['situacao'] = 'Ruim'
    return turma


print(notas(3.5, 2, 6.5, situacao=True))