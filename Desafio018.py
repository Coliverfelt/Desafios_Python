# Exercício Python 018: Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = float(input('Ângulo °: '))

print('Seno de {}° = {:.2f}'.format(angulo, sin(radians(angulo))))
print('Cos de {}° = {:.2f}'.format(angulo, cos(radians(angulo))))
print('Tangente de {}° = {:.2f}.'.format(angulo, tan(radians(angulo))))