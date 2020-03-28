# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = list()
somaPar = somaTerceiraColuna = maiorSegundaLinha = 0

for i in range(0, 3):
    for j in range(0, 3):
        matriz.append(int(input(f'Insira um valor para [{i}][{j}]: ')))

print('=-=' * 10)
print('{: ^30}'.format('MATRIZ'))
print('=-=' * 10)

k = 0
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[  {matriz[k + j]}  ]', end=' ')
        if matriz[k + j] % 2 == 0:
            somaPar += matriz[k + j]
        if j == 2:
            somaTerceiraColuna += matriz[k + j]
        if i == 1:
            if matriz[k + j] > maiorSegundaLinha:
                maiorSegundaLinha = matriz[k + j]
    print('')
    k += 3

print(f'A soma dos valores pares é {somaPar}.')
print(f'A soma dos valores da terceira coluna é {somaTerceiraColuna}.')
print(f'O maior valor da segunda linha é {maiorSegundaLinha}.')