# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = list()
listaIndex = list()
while True:
    valor = int(input('Digite um valor: '))
    lista.insert(0, valor)
    continuar = str(input('Quer continuar? [S/N]')).strip().lower()[0]
    if continuar == 'n':
        break
print(end='\n')
print('-==-' * 20)
for k, i in enumerate(lista):
    if i == 5:
        listaIndex.append(k + 1)
print(f'Foi/Foram digitado(s) {len(lista)} número(s).')
print(f'Lista: {lista}.')
lista.sort()
print(f'A lista de valores em ordem crescente é {lista}.')
lista.sort(reverse=True)
print(f'A lista de valores em ordem decrescente é {lista}.')
if listaIndex is not []:
    if len(listaIndex) == 1:
        print(f'O número 5 foi digitado na {listaIndex}º posição.')
    elif len(listaIndex) > 1:
        print(f'O número 5 foi digitado respectivamente nas posições {listaIndex}')
    else:
        print('O número 5 não foi digitado.')
else:
    print('O número 5 não foi digitado.')