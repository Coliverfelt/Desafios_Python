# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = list()
kmenor = kmaior = 0
for i in range(0, 5):
    valor = int(input('Digite um valor: '))
    if len(lista) == 0:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        if valor < lista[i - 1]:
            j = len(lista) - 1
            while valor <= lista[j]:
                kmenor = lista.index(lista[j])
                j -= 1
                if j < 0:
                    break
            lista.insert(kmenor, valor)
            print(f'Adicionado na posição {kmenor} da lista...')
        else:
            lista.insert(i, valor)
            print('Adicionado ao final da lista...')
    print(end='\n')
print('=-=' * 20)
print(f'Os valores digitados em ordem foram {lista}')