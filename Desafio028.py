# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(2)

if ((jogador >= 0) & (jogador <= 5)):
    if computador == jogador:
        print('PC: {}  Jogador: {}'.format(computador, jogador))
        print('Venceu!!')
    else:
        print('PC: {}  Jogador: {}'.format(computador, jogador))
        print('Perdeu!!')
else:
    print('O número tem que estar entre 0 e 5!')