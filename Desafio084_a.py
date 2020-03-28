# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

cadastro = list()
pessoa = list()
maisPesado = list()
maisLeve = list()

while True:
    pessoa.append(str(input('Nome: ')).strip().capitalize())
    pessoa.append(float(input('Peso: ')))
    cadastro.append(pessoa[:])
    if len(cadastro) == 1:
        maisLeve.append(pessoa[:])
        maisPesado.append(pessoa[:])
    else:
        if pessoa[1] >= maisPesado[0][1]:
            if pessoa[1] == maisPesado[0][1]:
                maisPesado.append(pessoa[:])
            else:
                for i in range(0, len(maisPesado)):
                    if pessoa[1] > maisPesado[i][1]:
                        del maisPesado[i]
                        maisPesado.insert(i, pessoa[:])
        elif pessoa[1] <= maisLeve[0][1]:
            if pessoa[1] == maisLeve[0][1]:
                maisLeve.append(pessoa[:])
            else:
                for i in range(0, len(maisLeve)):
                    if pessoa[1] < maisLeve[i][1]:
                        del maisLeve[i]
                        maisLeve.insert(i, pessoa[:])
    pessoa.clear()
    continua = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    while continua != 's' and continua != 'n':
        continua = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if continua == 'n':
        break

print('-=-' * 30)
for k, c in enumerate(cadastro):
    print(f'{k + 1}º: {c}')
print('-=-' * 30)

print(f'Você cadastrou {len(cadastro)} pessoas.')
if len(maisLeve) == 1:
    print(f'O peso mais leve foi {maisLeve[0][1]}kg. Peso de {maisLeve[0][0]}')
else:
    print(f'O peso mais leve foi {maisLeve[0][1]}kg. Pesos de', end=' ')
    for i in range(0, len(maisLeve)):
        print(f'{maisLeve[i][0]}', end='')
        if i == len(maisLeve) - 2:
            print(' e', end=' ')
        elif i == len(maisLeve) - 1:
            print('.')
        else:
            print(',', end=' ')
if len(maisPesado) == 1:
    print(f'O peso mais leve foi {maisPesado[0][1]}kg. Peso de {maisPesado[0][0]}')
else:
    print(f'O peso mais leve foi {maisPesado[0][1]}kg. Pesos de', end=' ')
    for i in range(0, len(maisPesado)):
        print(f'{maisPesado[i][0]}', end='')
        if i == len(maisPesado) - 2:
            print(' e', end=' ')
        elif i == len(maisPesado) - 1:
            print('.')
        else:
            print(',', end=' ')
