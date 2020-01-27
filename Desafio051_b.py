# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.

primeiroTermo = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))

decimoTermo = primeiroTermo + (10 - 1) * razao

print('A Prograssão Aritmética desenvolvida foi:')
for i in range(primeiroTermo, decimoTermo + razao, razao):
    print('{}'.format(i), end='; ')