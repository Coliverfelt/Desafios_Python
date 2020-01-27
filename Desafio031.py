# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distância da viagem (Km)? '))

if ((distancia >= 0.0) & (distancia <= 200.0)):
    print('O valor da passagem é R${:.2f}.'.format(distancia * .5))
else:
    print('O valor da passagem é R${:.2f}.'.format(distancia * .45))

preco = distancia * 0.5 if ((distancia >= 0.0) & (distancia <= 200.0)) else distancia * 0.45
print(preco)