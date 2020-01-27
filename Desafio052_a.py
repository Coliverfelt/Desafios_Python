# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Insira um número: '))

if (n > 1) and (n % 1 == 0) and (n % n == 0) and (n % 2 != 0) and (n % 3 != 0) and (n % 5 != 0) and (n % 7 != 0):
    print('É PRIMO!')
elif (n == 2) or (n == 3) or (n == 5) or (n == 7):
    print('É PRIMO!')
else:
    print('Não é PRIMO!')