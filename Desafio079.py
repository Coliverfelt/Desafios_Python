lista = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        valor = int(input('Esse número já existe na lista! Digite outro valor: '))
    lista.append(valor)
    print(f'Valor {valor} adicionado com sucesso!')
    continuar = str(input('Deseja continuar? [S/N]')).lower().strip()[0]
    while continuar not in 'sn':
        continuar = str(input('Por favor, digite apenas S ou N. Deseja continuar? [S/N]')).lower().strip()[0]
    if continuar in 'n':
        break
lista.sort()
print(f'Lista (CRESCENTE): {lista}')