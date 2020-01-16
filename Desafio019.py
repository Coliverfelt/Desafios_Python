# Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#                       Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

aluno1 = str(input('Aluno 1: '))
aluno2 = str(input('Aluno 2: '))
aluno3 = str(input('Aluno 3: '))
aluno4 = str(input('Aluno 4: '))

print('Sorteado: {}.'.format(choice([aluno1, aluno2, aluno3, aluno4])))
