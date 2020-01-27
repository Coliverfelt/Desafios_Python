# Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Digite a velocidade (KM): '))

if velocidade > 80:
    print('Você foi multado por exceder 80 Km/h!')
    kmmais = velocidade - 80.0
    print('A multa será no valor de R${:.2f}.'.format(kmmais * 7))
print('Tenha um bom dia! Dirija com segurança!')