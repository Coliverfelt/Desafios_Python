# Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = str(input('Digite um número de 0 a 9999: ')).zfill(4)

print('Seu número é: {}'.format(numero))
print("""
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}
""".format(numero[3], numero[2], numero[1], numero[0]))