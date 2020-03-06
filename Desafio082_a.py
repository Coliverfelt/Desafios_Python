# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    continua = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if continua == 'n':
        break
    while continua != 's':
        continua = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
        if continua == 'n':
            break
listaPar = list()
listaImpar = list()
for i in lista:
    if i % 2 == 0:
        listaPar.append(i)
    else:
        listaImpar.append(i)
# for i, v in enumerate(lista):
#     if v % 2 == 0:
#         listaPar.append(v)
#     elif v % 2 == 1:
#         listaImpar.append(v)
print('=-=' * 30)
print(f'Lista: {lista}')
print(f'Lista dos pares: {listaPar}')
print(f'Lista dos ímpares: {listaImpar}')