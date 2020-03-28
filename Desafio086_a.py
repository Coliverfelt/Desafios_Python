# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3
# e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = list()

for i in range(0, 3):
    for j in range(0, 3):
        matriz.append(int(input(f'Insira um valor para [{i}][{j}]: ')))
k = 0
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[  {matriz[k + j]}  ]', end=' ')
    print('')
    k += 3