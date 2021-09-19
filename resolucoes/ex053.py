# Leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.]
frase = str(input('Digite uma frase: ')).strip().replace(' ', '').upper()
invertida = ''
for letra in range(len(frase) - 1, -1, -1):
    invertida += frase[letra]
print(f'O contrario de {frase} é {invertida}.')
if frase == invertida:
    print('Essa frase É um palíndromo!')
else:
    print('Essa frase NÃO é um palíndromo.')
# SOLUÇÃO + ou - DO PROFESSOR /\
frase = str(input('Digite uma frase: ')).strip().replace(' ', '').upper()
print(f'O contrario de {frase} é {frase[::-1]}.')
if frase == frase[::-1]:
    print('Essa frase É um palíndromo!')
else:
    print('Essa frase NÃO é um palíndromo.')
