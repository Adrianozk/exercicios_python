# lista = []
# maior = menor = 0
# for i in range(1, 6):
#     numero = int(input('Digite um número: '))
#     if i == 1:
#         lista.append(numero)
#         print('Número adicionado no final da lista')
#     else:
#         for i in range(0, len(lista) + 1):
#             if i == 0:
#                 maior = numero
#                 menor = numero
#             else:
#                 if numero > maior:
#                     maior = numero
#                     lista.append(numero)
#                     print('Número adicionado no final da lista')
#                 if numero < menor:
#                     menor = numero
#                     lista.insert(0, numero)
#                     print('Número adicionado na posição 0 da lista')

# ============================= ↑ MINHA TENTATIVA BREVE DE RESOLVER ↑ ============================

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados foram {lista}')

# ============================= ↑ SOLUÇÃO DO PROFESSOR ↑ ============================