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

i = 0
print('\033[1;34m-\033[m' * 45)
print('\033[1;33m{:^45}\033[m'.format('LISTAGEM DE PREÇOS'))
print('\033[1;34m-\033[m' * 45)
while i < len(listagem):
    print(f'\033[1;35m{listagem[i]}\033[m', end='')
    print('\033[1;36m{}\033[m'.format('.' * (35 - len(listagem[i]))), end='')
    print(f'\033[1;32mR$ {listagem[i + 1]:6.2f}\033[m')
    i += 2
print('\033[1;34m-\033[m' * 45)