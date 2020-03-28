# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = somaTerceiraColuna = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Insira um valor para a posição [{l}][{c}]: '))
        if (l == 1) and (c == 0):
            maiorSegundaLinha = matriz[l][c]

print('=-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[  {matriz[l][c]}  ]', end=' ')
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
        if c == 2:
            somaTerceiraColuna += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maiorSegundaLinha:
                maiorSegundaLinha = matriz[l][c]
    print()

print('=-=' * 20)
print(f'A soma dos valores pares é {somaPar}.')
print(f'A soma dos valores da terceira coluna é {somaTerceiraColuna}.')
print(f'O maior valor da segunda linha é {maiorSegundaLinha}.')