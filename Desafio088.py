# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

jogos = list()
jogo = list()

print('-' * 40)
print('{:^40}'.format('JOGA NA MEGA SENA'))
print('-' * 40)

quantidadeJogos = int(input('Quantos jogos você deseja sortear? '))

frase = 'SORTEANDO'
print('-=-' * 13)
print(f'{frase:>19} {quantidadeJogos} JOGOS')
print('-=-' * 13)
for i in range(quantidadeJogos, 0, -1):
    for j in range(0, 6):
        rand = randint(0, 60)
        while rand in jogo:
            rand = randint(0, 60)
        jogo.append(rand)
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()

for i in range(0, quantidadeJogos):
    print(f'Jogo {i + 1}: {jogos[i]}')
    sleep(1)
print('-=-' * 13)
print('{:^39}'.format('BOA SORTE!'))
print('-=-' * 13)