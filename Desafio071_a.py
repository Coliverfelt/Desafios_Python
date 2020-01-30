# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

nomeDoBanco = 'BANCO JUSTO'
print('=-=' * 20)
print(f'{nomeDoBanco:^57}')
print('=-=' * 20)

valorSaque = int(input('Valor do Saque R$'))
valor = valorSaque
cont50 = cont20 = cont10 = cont1 = 0
while True:
    if valor % 50 == 0:
        cont50 += 1
        valor -= 50
    elif valor % 20 == 0:
        cont20 += 1
        valor -= 20
    elif valor % 10 == 0:
        cont10 += 1
        valor -= 10
    elif valor % 1 == 0:
        cont1 += 1
        valor -= 1
    if valor == 0:
        if cont50 > 0:
            print(f'Total de {cont50:2} cédulas de R$50.')
        if cont20 > 0:
            print(f'Total de {cont20:2} cédulas de R$20.')
        if cont10 > 0:
            print(f'Total de {cont10:2} cédulas de R$10.')
        if cont1 > 0:
            print(f'Total de {cont1:2} cédulas de R$1.')
        break
print('Volte sempre ao BANCO JUSTO! Tenha um Bom Dia!')