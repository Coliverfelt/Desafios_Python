# Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um número de 0 a 9999: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('Seu número é: {}'.format(numero))
print("""
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}
""".format(unidade, dezena, centena, milhar))