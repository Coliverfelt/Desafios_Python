# Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    cont = 0
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('=-=' * 20)
    if valor < 0:
        break
    for i in range(cont, 11):
        print(f'{cont:2} x {valor} = {cont * valor:2}')
        cont += 1
    print('=-=' * 20)
print('Pragrama Tabuada Encerrado. Volte Sempre!')