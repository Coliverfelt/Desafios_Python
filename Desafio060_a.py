# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input('Digite um número: '))

fatorial = 1

print('{:_^10}{}!{:_^10}'.format('\033[7m', numero, '\033[m'))
for i in range(numero, 0, -1):
    if i >= 1:
        if i == 1:
            print('{} '.format(i), end='')
        else:
            print('{} * '.format(i), end='')
    fatorial = fatorial * i

print('= {}'.format(fatorial))
