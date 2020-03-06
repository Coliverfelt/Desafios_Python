# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = list()
kmenor = kmaior = 0
for i in range(0, 5):
    valor = int(input('Digite um valor: '))
    if len(lista) == 0:
        lista.append(valor)
        print(f'\n{i}º: {valor}')
    else:
        if valor >= lista[i - 1]:
            for j in range(0, 1):
                for m in range(0, len(lista)):
                    if valor > lista[m]:
                        print(end='\n')
                        # print(valor, ' > ', lista[m])
                        kmaior = lista.index(lista[m])
            lista.insert(kmaior + 1, valor)
            print(f'{kmaior + 1}º: {valor}')
        else:
            for j in range(0, 1):
                for m in range(len(lista) - 1, -1, -1):
                    if valor <= lista[m]:
                        print(end='\n')
                        # print(valor, ' <= ', lista[m])
                        kmenor = lista.index(lista[m])
            lista.insert(kmenor, valor)
            print(f'{kmenor}°: {valor}')
    print('=-=' * 30)
    print(f'Lista: {lista}')
    print(end='\n')