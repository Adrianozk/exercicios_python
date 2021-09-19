def fatorial(n, show=False):
    strRetorno = ''
    fatorial = 1
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    if show:
        while n > 0:
            fatorial *= n
            if n != 1:
                strRetorno += str(n) + ' x '
            else:
                strRetorno += str(n) + ' = ' + str(fatorial)
            n -= 1
        return strRetorno
    else:
        while n > 0:
            fatorial *= n
            n -= 1
        return fatorial


print(fatorial(7, True))