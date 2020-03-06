# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = list()
maior = menor = 0
for v in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {v}: ')))
    if v == 0:
        maior = menor = lista[v]
    else:
        if lista[v] > maior:
            maior = lista[v]
        if lista[v] < menor:
            menor = lista[v]
print('=-=' * 30)
print(f'''Lista: {lista}''')
print(f'O MENOR valor {menor} está na(s) posição(ões): ', end='')
for k, v in enumerate(lista):
    if lista[k] == menor:
        print(f'{k}', end='; ')
print(end='\n')
print(f'O MAIOR valor {maior} está na(s) posição(ões): ', end='')
for k, v in enumerate(lista):
    if lista[k] == maior:
        print(f'{k}', end='; ')