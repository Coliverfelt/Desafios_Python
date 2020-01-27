# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

n = int(input('Quantos elementos da sequência de Fibonacci você deseja visualizar?'))

i = 3
anterior = 1
anteriorAnterior = 0

print('{}; {}; '.format(0, 1), end='')
while i <= n:
    fibonacci = anterior + anteriorAnterior
    print('{}; '.format(fibonacci), end='')
    anteriorAnterior = anterior
    anterior = fibonacci
    i += 1