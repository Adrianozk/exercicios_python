from datetime import datetime
def voto(ano):
    idade = datetime.today().year - ano
    if 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: Não vota.'


print(voto(int(input('Ano de nascimento: '))))