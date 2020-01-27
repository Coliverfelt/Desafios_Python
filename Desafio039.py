# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoNascimento = str(input('Digite o seu ano de nascimento: '))

tamanho = len(anoNascimento)

if (int(tamanho) > 4) or (int(tamanho) < 4):
    print('Não é possível realizar os cálculos com esta quantidade de dígitos.')

elif (int(tamanho) == 4):
    anoNascimento = int(anoNascimento)
    anoAtual = date.today().year
    idade = anoAtual - anoNascimento
    tempoAlista = idade - 18

    if idade < 18:
       print('Você precisará se alistar em {} anos.'.format((tempoAlista * (-1))))
    elif idade > 18:
       print('Seu tempo de alistamento ultrapassou {} anos.'.format(tempoAlista))
    elif idade == 18:
        print('Sua idade ({} anos), é a apropriada para o alistamento.'.format(idade))