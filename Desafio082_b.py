# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = list()
listaPar = list()
listaImpar = list()
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor % 2 == 0:
        listaPar.append(valor)
    else:
        listaImpar.append(valor)
    continua = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if continua == 'n':
        break
    while continua != 's':
        continua = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
        if continua == 'n':
            break
print('=-=' * 20)
print(f'Lista: {lista}')
print(f'Lista dos pares: {listaPar}')
print(f'Lista dos ímpares: {listaImpar}')