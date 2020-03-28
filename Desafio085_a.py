# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

lista = list()
listaPar = list()
listaImpar = list()

for i in range(0, 7):
    numero = int(input(f'Digite {i + 1}° valor: '))
    if numero % 2 == 0:
        listaPar.append(numero)
    else:
        listaImpar.append(numero)
    listaPar.sort()
    listaImpar.sort()
lista.append(listaPar[:])
lista.append(listaImpar[:])
print(f'Os valores pares digitados foram {listaPar}.')
print(f'Os valores pares digitados foram {listaImpar}.')