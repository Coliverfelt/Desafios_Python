# Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = input('Digite sua cidade: ').strip()

cidade = cidade.split()

print('Começa com SANTO? \n{}'.format('santo' in cidade[0].lower()))