# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite um terceiro número: '))

maior = n1
menor = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print('O maior número entre {}, {} e {} é: {}'.format(n1, n2, n3, maior))
print('O menor número entre {}, {} e {} é: {}'.format(n1, n2, n3, menor))