# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

cont = 0
print('=-=' * 20)
print('Estou pensando em um número de 1 a 10...')
print('=-=' * 20)
sleep(2)
computador = randint(1, 10)
print('\nPensei em um número!!')

acertou = False
while not acertou:
    humano = int(input('Adivinha qual é?!\n'))
    cont += 1
    if humano == computador:
        acertou = True

print('Parabéns!!! O número que pensei foi {} mesmo!'.format(computador))
if cont > 1:
    print('E você levou {} tentativa para acertar!'.format(cont))
else:
    print('E você acertou de primeira!'.format(cont))