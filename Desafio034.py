# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu salário: R$'))

if salario > 1250.0:
    print('Seu salário com um aumento de 10% é R${:.2f}.'.format((salario + (salario * 0.1))))
else:
    print('Seu salário com aumento de 15% é R${:.2f}.'.format((salario + (salario * 0.15))))