# Exercício Python 026: Faça um programa que leia uma frase pelo teclado
# e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez
# e em que posição ela aparece a última vez.

frase = input('Digite uma frase: ').strip()

print('A letra ''"a"'' aparece {} vezes.'.format(frase.lower().count('a', 0, )))
print('A letra ''"a"'' aparece pela primeira vez na posição {}.'.format(frase.lower().find('a') + 1))
print('A letra ''"a"'' aparece pela última vez na posição {}.'.format(frase.lower().rfind('a') + 1))