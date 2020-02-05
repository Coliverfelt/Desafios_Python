# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))
d = int(input('Digite um valor: '))
tupla = (a, b, c, d)
print(type(tupla))
print(f'Você digitou os valores: {tupla}')
print(f'O número 9 aparece {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O primeiro valor 3 foi digitado na posição {tupla.index(3) + 1}.')
else:
    print('O valor 3 não foi encontrado em nenhuma posição.')
cont = 0
for t in range(0, 4):
    if tupla[t] % 2 == 0:
        cont += 1
if cont == 1:
    for t in range(0, 4):
        if tupla[t] % 2 == 0:
            print(f'O único número par digitado foi: {tupla[t]}')
elif cont > 1:
    print(f'Os números pares foram:', end=' ')
    for t in range(0, 4):
        if tupla[t] % 2 == 0:
            print(f'{tupla[t]}', end=' ')
if cont == 0:
    print('Você não digitou números pares.')