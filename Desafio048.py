# Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
print('Ímpares múltiplos de 3:')
for x in range(1, 501, 2):
    if x % 3 == 0:
        print('{};'.format(x), end=' ')
        soma = soma + x
        cont += 1

print('\n\nA soma dos ímpares múltiplos de três é: {}.'.format(soma))
print('Foram calculados {} números.'.format(cont))