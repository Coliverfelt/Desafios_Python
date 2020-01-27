# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

n = int(input('Quantos elementos da sequência de Fibonacci você deseja visualizar?'))

i = 0

while i < n:
    if i == 0 or i == 1:
        print('{}; '.format(i), end='')
        ant = 1
        ant2 = 0
    else:
        fibonacci = ant + ant2
        print('{}; '.format(fibonacci), end='')
        ant2 = ant
        ant = fibonacci
    i += 1