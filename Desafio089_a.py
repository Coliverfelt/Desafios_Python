# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e
# permita que o usuário possa mostrar as notas de cada aluno individualmente.

import tabulate
from time import sleep
# alunos[[nome1,[nota1, nota2]], [nome2, [nota1, nota2]]]
alunos = []
nomes = []
notas = []

while True:
    nomes.append(str(input('Nome: ')).strip().capitalize())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    nomes.append(notas[:])
    alunos.append(nomes[:])
    continua = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    while continua not in 'sn':
        continua = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if continua == 'n':
        break
    nomes.clear()
    notas.clear()

# for i in range(0, len(alunos)):
#     if i == 0:
#         print(f'''
#     _________________________
#     |  Aluno: {alunos[i][0]:7}      |
#     |  Nota 1: {alunos[i][1][0]:10}  |
#     |  Nota 2: {alunos[i][1][1]:10}  |
#     -------------------------
#         ''')
#     if i == (len(alunos) - 1):
#         print(f'''
#     -------------------------
#     |  Aluno: {alunos[i][0]:7}      |
#     |  Nota 1: {alunos[i][1][0]:10}  |
#     |  Nota 2: {alunos[i][1][1]:10}  |
#     _________________________
#             ''')
#     else:
#         print(f'''
#     -------------------------
#     |  Aluno: {alunos[i][0]:7}      |
#     |  Nota 1: {alunos[i][1][0]:10}  |
#     |  Nota 2: {alunos[i][1][1]:10}  |
#     -------------------------
#             ''')

frase = 'BOLETIM'
print('-=-' * 14)
print(f'{frase:^40}')
print('-=-' * 14)

print(f'{"N°":^10}', end=' ')
print(f'{"Nome":^7}', end=' ')
print(f'{"Média":^17}')
print(f'{"_":_^35}')

for i in range(0, len(alunos)):
    print(f'{i + 1:^10}', end=' ')
    print(f'{alunos[i][0]:<10}', end=' ')
    print(f'{((alunos[i][1][0] + alunos[i][1][1]) / 2):^10}')
print(f'{"_":_^35}')

while True:
    mostrarNota = int(input('Mostrar as notas de qual aluno? (999 interrompe) '))
    while (mostrarNota <= 0) or (mostrarNota > len(alunos)):
        if mostrarNota == 999:
            break
        print(f'FAVOR INSERIR NÚMEROS ENTRE 1 e {len(alunos)}!!')
        mostrarNota = int(input('Mostrar as notas de qual aluno? (999 interrompe) '))
    if mostrarNota == 999:
        break
    print(f'As notas de {alunos[mostrarNota - 1][0]} são: [{alunos[mostrarNota - 1][1][0]}, {alunos[mostrarNota - 1][1][1]}]')
print('FINALIZANDO...')
sleep(0.5)
print('<<< VOLTE SEMPRE >>>')