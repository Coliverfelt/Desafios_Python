# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção Inteira.

n = float(input('Digite um número real: '))
print('A parte inteira de {} é {}.'.format(n, int(n)))