# Exercício Python 050: Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0

print('Digite 6 números: ')

for i in range(1, 7):
    n = int(input())
    if n % 2 == 0:
        soma = soma + n
        cont += 1
print('O somatório dos {} valores pares dos 6 que você inseriu é: {}.'.format(cont, soma))