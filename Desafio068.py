# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from time import sleep
from random import randint

print('=-=' * 10)
print('Vamo jogar PAR ou ÍMPAR!')
print('=-=' * 10)
sleep(1)
vitoria = 0
while True:
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Você escolhe PAR ou ÍMPAR? [P|I]')).strip().upper()[0]
    print('Ok! Agora deixe-me pensar em um número...')
    sleep(0.5)
    computador = randint(0, 10)
    jogador = int(input('Pensei! Me diga agora qual é o seu: '))

    print('*' * 18)
    print(f'* Computador = {computador} *')
    print(f'* Jogador = {jogador}    *')
    print('* DEU PAR        *' if (computador + jogador) % 2 == 0 else '* DEU ÍMPAR      *')
    print('*' * 18)
    
    if ((computador + jogador) % 2 == 0) and escolha in 'I':
        print('Ops.. Você perdeu!')
        break
    elif ((computador + jogador) % 2 != 0) and escolha in 'P':
        print('Ops.. Você perdeu!')
        break
    else:
        vitoria += 1
        print('PARABÉNS! Vamos de novo!')
print(f'Você ganhou {vitoria} vezes consecutivas.')