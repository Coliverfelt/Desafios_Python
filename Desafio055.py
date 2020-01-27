# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

peso0 = float(input('Peso: '))

maior = peso0
menor = peso0

for i in range(0, 4):
    peso = float(input('Peso: '))

    if peso >= maior:
        maior = peso
    elif peso <= menor:
        menor = peso

print('O maior peso é: {:.2f}.'.format(maior))
print('O menor peso é: {:.2f}.'.format(menor))