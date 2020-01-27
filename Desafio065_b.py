# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

opcao = 's'
soma = cont = maior = menor = 0

while opcao in 's':
    numero = int(input('Digite um número: '))
    opcao = str(input('Deseja continuar digitando? [S/N]')).strip().lower()

    soma += numero
    cont += 1
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print('A soma dos valores digitados é {}.'.format(soma))
print('A média dos valores digitados é {}.'.format(float(soma / cont)))
print('O maior valor é {}.'.format(maior))
print('O menor valor é {}.'.format(menor))