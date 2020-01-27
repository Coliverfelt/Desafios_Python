# Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

co = float(input('Cateto Oposto: '))
ca = float(input('Cateto adjacente: '))

h = ((co ** 2) + (ca ** 2)) ** (1/2)

print('O valor da hipotenusa é: {:.2f}'.format(h))
print('O valor da hipotenusa é: {:.0f}'.format(h))