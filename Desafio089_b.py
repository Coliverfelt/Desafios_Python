# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e
# permita que o usuário possa mostrar as notas de cada aluno individualmente.

cadastro = []

while True:
    nome = str(input('Nome: ')).strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = ((nota1 + nota2) / 2)
    cadastro.append([nome, [nota1, nota2], media])

    continua = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    while continua not in 'sn':
        continua = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if continua in 'n':
        break

print('=-=' * 10, 'CADASTRO', '=-=' * 10)

print(f'{"N°":<4}', end='')
print(f'{"Nome":<10}', end='')
print(f'{"Média":<8}', end='')
print()
print('-' * 20)

for k, aluno in enumerate(cadastro):
    print(f'{k + 1:<4}', end='')
    print(f'{aluno[0]:<10}', end='')
    print(f'{aluno[2]:<8.2f}', end='')
    print()