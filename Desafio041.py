# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date

anoNascimento = int(input('Insira seu ano de nascimento: '))
anoAtual = date.today().year

idade = anoAtual - anoNascimento

if ((idade >= 0) and (idade <= 9)):
    print('Você tem {} anos e está na categoria MIRIM!'.format(idade))
elif ((idade > 9) and (idade <= 14)): #elif idade <= 14:
    print('Você tem {} anos e está na categoria INFANTIL!'.format(idade))
elif ((idade > 14) and (idade <= 19)): #elif idade <= 19:
    print('Você tem {} anos e está na categoria JUNIOR!'.format(idade))
elif idade <= 25: #elif idade <= 25
    print('Você tem {} anos e está na categoria SÊNIOR!'.format(idade))
elif idade > 20: #else: #elif idade > 25:
    print('Você tem {} anos e está na categoria MASTER!'.format(idade))