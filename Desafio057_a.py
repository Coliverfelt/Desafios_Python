#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite seu sexo: [F/M]')).upper()

while (sexo != 'F') and (sexo != 'M'):
    print('Desculpe, mas só aceitamos as letras "F" ou "M".')
    print('Tente novamente!')
    sexo = str(input('Digite seu sexo: [F/M]')).upper()

if sexo == 'F':
    print('Entendi! Você é do sexo Feminino.')
else:
    print('Entendi! você é do sexo Masculino.')