# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

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
print('=-=' * 30)
print(f'Lista (CRESCENTE): {lista}')