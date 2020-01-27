# Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva
# para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
import emoji

cores = {'limpa': '\033[m',
         'p&b': '\033[7m',
         'ciano&sub': '\033[4:36m',
         'amarelo&neg3': '\033[1:33m',
         'vermelho&neg': '\033[1:31m',
         'azul&neg': '\033[1:34m',
         'verde&neg': '\033[1:32m'}

print('{}{:_^50}{}'.format(cores['p&b'], 'Contagem regressiva:', cores['limpa']))
for c in range(10, -1, -1):
    if c == 3:
        print('{}{: ^25}{}'.format(cores['vermelho&neg'], c, cores['limpa']))
    elif c == 2:
        print('{}{: ^25}{}'.format(cores['azul&neg'], c, cores['limpa']))
    elif c == 1:
        print('{}{: ^25}{}'.format(cores['verde&neg'], c, cores['limpa']))
    elif c == 0:
        print('{}{: ^25}{}'.format(cores['p&b'], c, cores['limpa']))
    else:
        print('{: ^25}'.format(c))
    sleep(1)
print(emoji.emojize('{}FELIZ ANO NOVO{}{}!!!{} :dizzy:'.format(cores['ciano&sub'], cores['limpa'], cores['amarelo&neg3'], cores['limpa']), use_aliases=True))