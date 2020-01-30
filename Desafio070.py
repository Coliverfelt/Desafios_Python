# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = cont = maisBarato = 0
nomeDaLoja = 'LOJA SUPER BARATÃO'
print('=-=' * 20)
#print('{:^23.5}LOJA SUPER BARATÃO{:^23.5}'.format('', ''))
print(f'{nomeDaLoja:^57}')
print('=-=' * 20)
while True:
    continua = ' '
    nome = str(input('Nome do produto: ')).strip().title()
    preco = float(input('Preço: R$'))
    total += preco
    if (maisBarato == 0) or (preco < maisBarato):
        maisBarato = preco
        maisBaratoNome = nome
    if preco > 1000:
        cont += 1
    while continua not in 'sn':
        continua = str(input('Deseja continuar? [S|N] ')).strip().lower()[0]
    if continua == 'n':
        break
print(f'''
Total R${total:.2f}.
{cont} produtos custam mais que R$1000.00.
O produto mais barato é {maisBaratoNome} que custa {maisBarato:.2f}.
''')