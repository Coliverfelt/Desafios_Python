# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input('Digite um número: '))

fatorial = 1

print('{:_^20}{}!{:_^20}'.format('\033[7m', numero, '\033[m'))

while numero >= 1:
    if numero != 1:
        print('{} * '.format(numero), end='')
    elif numero == 1:
        print('{} = '.format(numero), end='')
        print('{}'.format(fatorial))
    fatorial *= numero
    numero -= 1
