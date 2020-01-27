# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input('Peso (Kg): '))
altura = float(input('Altura (m): '))

imc = (peso / (pow(altura, 2))) #imc = peso / (altura ** 2)

if imc < 18.5:
    print('IMC: {:.2f}.'.format(imc))
    print('Você está abaixo do peso!')
elif ((imc >= 18.5) and (imc <= 25)):
    print('IMC: {:.2f}.'.format(imc))
    print('Você está no peso ideal!')
elif ((imc > 25) and (imc <= 30)):
    print('IMC: {:.2f}.'.format(imc))
    print('Você está com sobrepeso!')
elif ((imc > 30) and (imc <= 40)):
    print('IMC: {:.2f}.'.format(imc))
    print('Você está obeso!')
elif imc > 40:
    print('IMC: {:.2f}.'.format(imc))
    print('Você está com obesidade mórbida!')