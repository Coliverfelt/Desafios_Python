# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3
# e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

linha1 = list()
linha2 = list()
linha3 = list()

for i in range(0, 3*3):
    if 0 <= i <= 2:
        linha1.append(int(input(f'Insira um valor para [0][{i}]: ')))
    elif 3 <= i <= 5:
        if i == 3:
            linha2.append(int(input(f'Insira um valor para [1][{i - 3}]: ')))
        elif i == 4:
            linha2.append(int(input(f'Insira um valor para [1][{i - 3}]: ')))
        elif i == 5:
            linha2.append(int(input(f'Insira um valor para [1][{i - 3}]: ')))
    elif 6 <= i <= 9:
        if i == 6:
            linha3.append(int(input(f'Insira um valor para [2][{i - 6}]: ')))
        elif i == 7:
            linha3.append(int(input(f'Insira um valor para [2][{i - 6}]: ')))
        elif i == 8:
            linha3.append(int(input(f'Insira um valor para [2][{i - 6}]: ')))
print('*' * 10, end=' ')
print('MATRIZ', end=' ')
print('*' * 10, end='\n')
for k, v in enumerate(linha1):
    print(f'[  {linha1[k]}  ]', end=' ')
print('')
for k, v in enumerate(linha2):
    print(f'[  {linha2[k]}  ]', end=' ')
print('')
for k, v in enumerate(linha3):
    print(f'[  {linha3[k]}  ]', end=' ')
print('')