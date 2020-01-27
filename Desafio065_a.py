# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

numero = int(input('Digite um número: '))
opcao = str(input('Deseja continuar digitando? [S/N]')).strip().lower()
if opcao not in 'sn':
    print('Por favor digite apenas S ou N.')
    exit()
else:
    soma = numero
    cont = 1
    maior = numero
    menor = numero
    while opcao != 'n':
        numero = int(input('Digite um número: '))
        opcao = str(input('Deseja continuar digitando? [S/N]')).strip().lower()[0]
        if opcao != 's' and opcao != 'n':
            print('Por favor digite apenas S ou N.')
            exit()
        soma += numero
        cont += 1
        if numero >= maior:
            maior = numero
        elif numero <= menor:
            menor = numero
print('A soma dos valores digitados é {}.'.format(soma))
print('A média dos valores digitados é {}.'.format(float(soma / cont)))
print('O maior valor é {}.'.format(maior))
print('O menor valor é {}.'.format(menor))