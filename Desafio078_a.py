# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = list()

for v in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {v}: ')))

print('=-=' * 30)
print(f'''Lista: {lista}''')
print(f'O MENOR valor {min(lista)} está na(s) posição(ões): ', end='')
for k, v in enumerate(lista):
    if v == min(lista):
        print(f'{k}', end='; ')
print(end='\n')
print(f'O MAIOR valor {max(lista)} está na(s) posição(ões): ', end='')
for k, v in enumerate(lista):
    if v == max(lista):
        print(f'{k}', end='; ')