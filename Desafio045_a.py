# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
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

computador = choice(['pedra', 'papel', 'tesoura'])

print('Escolhi! Agora é sua vez...')

print('{}*{}'.format(cores['fundocinza'], cores['limpa']) * 20)
print('''
    {}ESCOLHA VOCÊ:{}
    
    {}1{} {}-{} {}Pedra{}
    {}2{} {}-{} {}Papel{}
    {}3{} {}-{} {}Tesoura{}'''.format(cores['fundovermelho'], cores['limpa'],
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
jogador = str(input()).strip()
jogador = jogador.lower()

print('\nComputador: {}'.format(computador))
print('Jogador: {}\n'.format(jogador))

if ((jogador != 'pedra') and (jogador != 'papel') and (jogador != 'tesoura')):
    print('Desculpe, mas não consegui reconhecer o que você digitou.\nTente novamente!')
else:
    if jogador == computador:
        print('Ops.. Empatamos!')
        print('Você escolheu {} e eu {}.'.format(jogador, computador))
    else:
        if ((jogador == 'pedra') and (computador == 'tesoura')):
            print('Não acredito!! Perdi =x')
            print('Você escolheu {} e eu {}.'.format(jogador, computador))
        elif ((jogador == 'pedra') and (computador == 'papel')):
            print('AHAAA! Te ganhei!')
            print('Você escolheu {} e eu {}.'.format(jogador, computador))
        elif ((jogador == 'tesoura') and (computador == 'pedra')):
            print('AHAAA! Te ganhei!')
            print('Você escolheu {} e eu {}.'.format(jogador, computador))
        elif ((jogador == 'papel') and (computador == 'pedra')):
            print('Não acredito!! Perdi =x')
            print('Você escolheu {} e eu {}.'.format(jogador, computador))
        elif ((jogador == 'papel') and (computador == 'tesoura')):
            print('AHAAA! Te ganhei!')
            print('Você escolheu {} e eu {}.'.format(jogador, computador))
        elif ((jogador == 'tesoura') and (computador == 'papel')):
            print('Não acredito!! Perdi =x')
            print('Você escolheu {} e eu {}.'.format(jogador, computador))