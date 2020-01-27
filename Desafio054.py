# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

count = 0

for i in range(0, 7):
    anoNascimento = int(input('Ano de nascimento: ').strip())
    anoNascimento = str(anoNascimento)

    if len(anoNascimento) != 4:
        print('Favor digitar 4 dígitos!')
        exit()
    else:
        anoNascimento = int(anoNascimento)
        if ((date.today().year - anoNascimento) >= 21):
            count += 1

print('{} pessoas já atingiram a maioridade.'.format(count))
print('{} pessoas ainda não atingiram a maioridade.'.format(7 - count))