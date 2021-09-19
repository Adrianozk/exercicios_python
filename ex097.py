def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f'{txt:^{len(txt) + 4}}')
    print('~' * (len(txt) + 4))


escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')