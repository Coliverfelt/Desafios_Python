# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número inteiro: '))
cores = {'limpa': '\033[m',
         'brancoevermelho': '\033[1:30:41m',
         'azul': '\033[1:34m',
         'amarelo': '\033[1:33m',
         'lilas': '\033[4:35m',
         'negativa': '\033[7m'}

print('{}ESCOLHA A BASE DE CONVERSÃO:{}'.format(cores['brancoevermelho'], cores['limpa']))
print('{}1{} {}-{} {}Binário{}'
      .format(cores['azul'], cores['limpa'],
              cores['amarelo'], cores['limpa'],
              cores['lilas'], cores['limpa']))
print('{}2{} {}-{} {}Octal{}'
      .format(cores['azul'], cores['limpa'],
              cores['amarelo'], cores['limpa'],
              cores['lilas'], cores['limpa']))
print('{}3{} {}-{} {}Hexadecimal{}'
      .format(cores['azul'], cores['limpa'], 
              cores['amarelo'], cores['limpa'], 
              cores['lilas'], cores['limpa']))

baseConversao = int(input('Escolha: '))

if baseConversao == 1:
    print(bin(numero)[2:])
elif baseConversao == 2:
    print(oct(numero)[2:])
elif baseConversao == 3:
    print(hex(numero)[2:])
else:
    print('\n{}Favor escolher entre 1 e 3!{}'.format(cores['negativa'], cores['limpa']))
