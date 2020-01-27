# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

cores = {
            'limpa': '\033[m',
            'negamarelo': '\033[1:33m',
            'negazul': '\033[1:34m'
}

v1 = float(input('Digite um valor: '))
v2 = float(input('Digite outro valor: '))

menu = 0

while menu != 5:
    menu = int(input('''
    {}[1]{} {}Somar{}
    {}[2]{} {}Multiplicar{}
    {}[3]{} {}Maior{}
    {}[4]{} {}Novos números{}
    {}[5]{} {}Sair do programa{}
    '''.format(cores['negamarelo'], cores['limpa'], cores['negazul'], cores['limpa'],
               cores['negamarelo'], cores['limpa'], cores['negazul'], cores['limpa'],
               cores['negamarelo'], cores['limpa'], cores['negazul'], cores['limpa'],
               cores['negamarelo'], cores['limpa'], cores['negazul'], cores['limpa'],
               cores['negamarelo'], cores['limpa'], cores['negazul'], cores['limpa']
               )))
    if menu == 1:
        print('{} + {} = {}'.format(v1, v2, v1 + v2))
    elif menu == 2:
        print('{} * {} = {}'.format(v1, v2, v1 * v2))
    elif menu == 3:
        maior = v1
        if v2 > maior:
            print('{} é maior que {}.'.format(v2, v1))
        elif v1 == v2:
            print('{} é igual a {}.'.format(v1, v2))
        else:
            print('{} é maior que {}.'.format(v1, v2))
    elif menu == 4:
        v1 = float(input('Digite um valor: '))
        v2 = float(input('Digite outro valor: '))
    elif menu == 5:
        print('Finalizando...')
    else:
        print('Oops! Tente novamente. Só aceitamos opções entre 1 e 5!')
    sleep(1)
exit()

