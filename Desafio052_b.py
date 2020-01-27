# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número  inteiro: '))
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[32m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(i), end=' ')

print('\n{}O número {} foi divisível {} vezes.'.format('\033[m', n, total))

if total == 2:
    print('{}Logo, É PRIMO!{}'.format('\033[7m', '\033[m'))
else:
    print('{}Logo, NÃO É PRIMO!{}'.format('\033[7m', '\033[m'))