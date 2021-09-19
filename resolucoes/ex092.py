from datetime import date
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
anoNascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = date.today().year - anoNascimento
pessoa['ctps'] = int(input('Carteira de trabalho(0 se não houver): '))
if pessoa['ctps'] != 0:
    pessoa['anoContratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['anoContratacao'] + 35 - anoNascimento
print()
for k, v in pessoa.items():
    print(f'{k}: {v}')