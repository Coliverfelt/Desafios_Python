# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Tupla: ', end='')
for t in tupla:
    print(f'{t}', end=' ')

menor = maior = tupla[0]
for i in range(1, len(tupla)):
    if tupla[i] < menor:
        menor = tupla[i]
    if tupla[i] > maior:
        maior = tupla[i]
print(f'''
Menor: {menor}
Maior: {maior}
''')
