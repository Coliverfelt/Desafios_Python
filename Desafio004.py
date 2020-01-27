# Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

cores = {'limpa': '\033[m',
         'negativo': '\033[7m',
         'azulebranco': '\033[1:30:44m',
         'azulevermelho': '\033[4:31:44m',
         'azuleverde': '\033[0:32:44m',
         'azuleamarelo': '\033[1:33:44m',
         'azulelilas': '\033[4:35:44m',
         'azuleciano': '\033[0:36:44m',
         'azulecinza': '\033[1:37:44m'
         }

x = input('Digite algo: ')

alpha = x.isalpha()
alnum = x.isalnum()
ascii = x.isascii()
decimal = x.isdecimal()
digit = x.isdigit()
identifier = x.isidentifier()
lower = x.islower()
numeric = x.isnumeric()
printable = x.isprintable()
space = x.isspace()
title = x.istitle()
upper = x.isupper()

tipo = type(x)

print('O tipo primitivo é: {}{}{}'.format(cores['negativo'], tipo, cores['limpa']))

if alpha:
    print('{}{}{}'.format(cores['azulebranco'], 'É alfábético.', cores['limpa']))
else:
    print('{}{}{}'.format(cores['azulevermelho'], 'Não é alfabético.', cores['limpa']))

if alnum:
    print('{}{}{}'.format(cores['azuleverde'], 'É alfanumérico.', cores['limpa']))
else:
    print('{}{}{}'.format(cores['azulevermelho'], 'Não é alfanumérico.', cores['limpa']))

if ascii:
    print('{}{}{}'.format(cores['azuleamarelo'], 'Faz parte da tabela ASCII.', cores['limpa']))
else:
    print('{}{}{}'.format(cores['azulevermelho'], 'Não faz parte da tabela ASCII.', cores['limpa']))

if decimal:
    print('{}{}{}'.format(cores['azulelilas'], 'É decimal.', cores['limpa']))
else:
    print('{}{}{}'.format(cores['azulevermelho'], 'Não é decimal.', cores['limpa']))

if digit:
    print('{}{}{}'.format(cores['azuleciano'], 'É um dígito.', cores['limpa']))
else:
    print('{}{}{}'.format(cores['azulevermelho'], 'Não é dígito.', cores['limpa']))

if identifier:
    print('{}{}{}'.format(cores['azulecinza'], 'É identificado.', cores['limpa']))
else:
    print('{}{}{}'.format(cores['azulevermelho'], 'Não é identificado.', cores['limpa']))

if lower:
    print('Possui apenas caracteres minúsculos.')
else:
    print('Não possui apenas caracteres minúsculos.')

if numeric:
    print('É numérico.')
else:
    print('Não é numérico.')

if printable:
    print('Pode ser impresso.')
else:
    print('Não pode ser impresso.')

if space:
    print('É um espaço.')
else:
    print('Não é um espaço.')

if title: #Capitalizada: Não está nem maiúscula nem minúscula
    print('É uma sequência capitalizada.')
else:
    print('Não é uma sequência capitalizada.')

if upper:
    print('Possui apenas caracteres maiúsculos.')
else:
    print('Não possui apenas caracteres maiúsculos.')
