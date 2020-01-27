# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

cores = {'limpa': '\033[m',
         'neglilas': '\033[1:35m',
         'negciano': '\033[1:36m',
         'fundocinza': '\033[1:47m',
         'fundovermelho': '\033[41m',
         'sublinhado': '\033[4m'}

print('{}*{}'.format(cores['fundocinza'], cores['limpa']) * 20)
print(' {}Deixa eu pensar...{}'.format(cores['fundovermelho'], cores['limpa']))
print('{}*{}'.format(cores['fundocinza'], cores['limpa']) * 20)
sleep(3)

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)

print('Escolhi! Agora é sua vez...')

print('{}*{}'.format(cores['fundocinza'], cores['limpa']) * 20)
print('''
    {}ESCOLHA VOCÊ:{}

    {}0{} {}-{} {}Pedra{}
    {}1{} {}-{} {}Papel{}
    {}2{} {}-{} {}Tesoura{}'''.format(cores['fundovermelho'], cores['limpa'],
                                      cores['neglilas'], cores['limpa'],
                                      cores['negciano'], cores['limpa'],
                                      cores['sublinhado'], cores['limpa'],
                                      cores['neglilas'], cores['limpa'],
                                      cores['negciano'], cores['limpa'],
                                      cores['sublinhado'], cores['limpa'],
                                      cores['neglilas'], cores['limpa'],
                                      cores['negciano'], cores['limpa'],
                                      cores['sublinhado'], cores['limpa']))
print('{}*{}'.format(cores['fundocinza'], cores['limpa']) * 20)
jogador = int(input())

print('\nComputador: {}'.format(itens[computador]))
print('Jogador: {}\n'.format(itens[jogador]))

if ((jogador != 0) and (jogador != 1) and (jogador != 2)):
    print('Desculpe, mas não consegui reconhecer o que você digitou.\nTente novamente!')
else:
    if jogador == computador:
        print('Ops.. Empatamos!')
        print('Você escolheu {} e eu {}.'.format(itens[jogador], itens[computador]))
    else:
        if ((jogador == 0) and (computador == 2)):
            print('Não acredito!! Perdi =x')
            print('Você escolheu {} e eu {}.'.format(itens[jogador], itens[computador]))
        elif ((jogador == 0) and (computador == 1)):
            print('AHAAA! Te ganhei!')
            print('Você escolheu {} e eu {}.'.format(itens[jogador], itens[computador]))
        elif ((jogador == 2) and (computador == 0)):
            print('AHAAA! Te ganhei!')
            print('Você escolheu {} e eu {}.'.format(itens[jogador], itens[computador]))
        elif ((jogador == 1) and (computador == 0)):
            print('Não acredito!! Perdi =x')
            print('Você escolheu {} e eu {}.'.format(itens[jogador], itens[computador]))
        elif ((jogador == 1) and (computador == 2)):
            print('AHAAA! Te ganhei!')
            print('Você escolheu {} e eu {}.'.format(itens[jogador], itens[computador]))
        elif ((jogador == 2) and (computador == 1)):
            print('Não acredito!! Perdi =x')
            print('Você escolheu {} e eu {}.'.format(itens[jogador], itens[computador]))