# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial

numero = int(input('Digite um número: '))
fatorial = factorial(numero)
print('{}! = '.format(numero), end='')
while numero >= 1:
    if numero != 1:
        print('{} * '.format(numero), end='')
    else:
        print('{} = '.format(numero), end='')
    numero -= 1

print(fatorial)