# Exercício Python 003: Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))

cores = {'limpa':'\033[m',
         'peb':'\033[7m',
         'brancoevermelho':'\033[0;30;42m',
         'brancoeeverde':'\033[0;30;42m',
         'brancoeamarelo':'\033[0;30;43',
         'brancoeazul':'\033[0;30;44m',
         'brancoelilas':'\033[0;30;45m',
         'brancoeciano':'\033[0;30;46m',
         'brancoecinza':'\033[0;30;47m'}
print('A soma entre {}{}{} e {}{}{} vale {}{}{}'.format(cores['peb'], n1, cores['limpa'], cores['brancoevermelho'],
                                                                      n2, cores['limpa'], cores['brancoeciano'],
                                                                      n1+n2, cores['limpa']))