lista = list()

for i in range(0, 5):
    j = 0
    valor = int(input('Digite um valor: '))
    if lista == [] or valor > max(lista):
        lista.append(valor)
        print(f'O valor {valor} foi adicionado ao último espaço da lista. Está na posição {lista.index(valor)}')
    while valor > lista[j]:
        j += 1
print(lista)
