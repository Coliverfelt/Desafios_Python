#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite seu sexo: [F/M]')).strip().upper()[0]

while sexo not in 'MmFf':
    print('Dados inválidos!')
    sexo = str(input('Por favor, digite seu sexo: [F/M]')).strip().upper()[0]

if sexo == 'F':
    print('Entendi! Você é do sexo Feminino.')
else:
    print('Entendi! você é do sexo Masculino.')