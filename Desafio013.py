# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Salario: '))
aumento = salario * (15/100)

print('O salario com aumento de 15% é R${:.2f}.'.format(salario + aumento))
