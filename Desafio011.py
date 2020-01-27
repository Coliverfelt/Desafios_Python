# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura = float(input('Altura (m): '))
largura = float(input('Largura (m): '))

area = altura * largura
litros = area / 2

print('A área é de {} m, e é necessário {} litros de tinta para pintá-la.'.format(area, litros))