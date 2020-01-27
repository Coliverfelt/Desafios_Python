# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numero = int(input('Digite um número: '))
print('Flag de parada: 999')

cont = 1
soma = numero

while numero != 999:
    numero = int(input('Digite um número: '))
    if numero != 999:
        print('Flag de parada: 999')
        cont += 1
        soma += numero

print('Você digitou {} números, e a soma entre eles é {}.'.format(cont, soma))
