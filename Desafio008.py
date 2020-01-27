# Exercício Python 008: Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.

valor = float(input('Digite um valor em metros: '))

c = valor * 100
mm = valor * 1000

print('O valor {} em centímetros é {}. \nO valor {} em metros é {}'.format(valor, c, valor, mm))