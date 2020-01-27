# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numero = int(input('Digite um número: '))
print('Flag de parada: 999')

cont = 1
soma = numero

numero = int(input('Digite um número: '))
while numero != 999:
    print('Flag de parada: 999')
    cont += 1
    soma += numero
    numero = int(input('Digite um número: '))

print('Você digitou {} números, e a soma entre eles é {}.'.format(cont, soma))
