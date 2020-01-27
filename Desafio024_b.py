# Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = input('Digite sua cidade: ').strip()

print('Começa com Santo? ', cidade[:5].upper() == 'SANTO')