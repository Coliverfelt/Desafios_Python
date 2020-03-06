# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = list()

for i in range(0, 5):
    valor = int(input('Digite um valor: '))
    if i == 0 or valor > lista[len(lista) - 1]: # i == lista [-1]
        lista.append(valor)
        print('Valor adicionado no final da lista...')
    else:
        posicao = 0
        while posicao < len(lista):
            if valor <= lista[posicao]:
                lista.insert(posicao, valor)
                print(f'Valor adicionado na posição {posicao} da lista...')
                break
            posicao += 1
print('=-=' * 20)
print(f'Os valores digitados em ordem foram {lista}')