# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoa = []
cadastro = []
maiorPeso = menorPeso = 0

while True:
    pessoa.append(str(input('Nome: ')).strip().capitalize())
    pessoa.append(float(input('Peso: ')))

    if len(cadastro) == 0:
        menorPeso = maiorPeso = pessoa[1]
    else:
        if pessoa[1] < menorPeso:
            menorPeso = pessoa[1]
        if pessoa[1] > maiorPeso:
            maiorPeso = pessoa[1]

    cadastro.append(pessoa[:])

    continua = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    while continua not in 'sn':
        continua = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if continua in 'n':
        break

    pessoa.clear()

print('=-=' * 30)
print(f'Você cadastrou {len(cadastro)} pessoas.')
cont = 0
print(f'O menor peso foi {menorPeso}kg de ', end='')
for p in cadastro:
    if p[1] == menorPeso:
        if cont == 0:
            print(f'{p[0]}', end='')
        else:
            print(f'; {p[0]}', end='')
        cont += 1
print()
cont = 0
print(f'O maior pefo foi {maiorPeso}kg de ', end='')
for p in cadastro:
    if p[1] == maiorPeso:
        if cont == 0:
            print(f'{p[0]}', end='')
        else:
            print(f'; {p[0]}', end='')
        cont += 1
print()