lista = list()
while True:
    valor = int(input('Digite um valor: '))
    while valor in lista:
        print('Esse número já existe na lista. Não poderei adicionar...')
        continuar = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
        while continuar not in 'sn':
            print('Desculpe, não entendi! Digite apenas S ou N...')
            continuar = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
        if continuar in 'n':
            break
        if continuar in 's':
            valor = int(input('Digite um valor: '))
    lista.append(valor)
    print(f'Valor {valor} adicionado à lista com sucesso!')
    continuar = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
    while continuar not in 'sn':
        print('Desculpe, não entendi! Digite apenas S ou N...')
        continuar = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
    if continuar in 'n':
        break
lista.sort()
print(f'Lista (CRESCENTE): {lista}')