# Faça um programa que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece da última vez

frase = input('Digite uma frase qualquer: ').strip()
print(f'A letra A aparece {frase.upper().count("A")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.upper().find("A") + 1}')
print(f'A última letra A apareceu na posição {frase.upper().rfind("A") + 1}')