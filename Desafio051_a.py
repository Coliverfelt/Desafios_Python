# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.

primeiroTermo = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))

pa = primeiroTermo + (10 - 1) * razao

print('PROGRESSÃO ARITMÉTICA: ')
for i in range(1, 11):
    print('{}; '.format(primeiroTermo + (i - 1) * razao), end='')

print('\n')

for i in range(primeiroTermo, pa + razao, razao):
    print('{}; '.format(i), end='')

print('\n')