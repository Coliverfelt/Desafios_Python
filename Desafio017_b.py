# Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
#                       Calcule e mostre o comprimento da hipotenusa.

from math import pow, sqrt, hypot, trunc

co = float(input('Cateto Oposto: '))
ca = float(input('Cateto adjacente: '))

print('O valor da hipotenusa é: {:.2f}'.format(sqrt(pow(co, 2) + pow(ca, 2))))
print('O valor da hipotenusa é: {}'.format(trunc(hypot(co, ca))))
