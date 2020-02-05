# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

print('\033[1;34m-\033[m' * 45)
print(f'\033[1;33m{"LISTAGEM DE PREÇOS":^45}\033[m')
print('\033[1;34m-\033[m' * 45)
for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f'\033[1;35m{listagem[posicao]:.<30}\033[m', end='')
    else:
        print(f'\033[1;32mR$ {listagem[posicao]:6.2f}\033[m')
print('\033[1;34m-\033[m' * 45)