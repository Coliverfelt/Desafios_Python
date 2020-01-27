# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

nome = str(input('Nome: ').strip())
idade = int(input('Idade: ').strip())
sexo = str(input('Sexo (F/M): ').strip().lower())

somaIdade = idade
homemMaisVelhoNome = nome
homemMaisVelhoIdade = idade
count = 0

if sexo == 'm':
    homemMaisVelhoIdade = idade
    homemMaisVelhoNome = nome
elif sexo == 'f':
    if idade < 20:
        count += 1

for i in range(0, 3):
    nome = str(input('Nome: ').strip())
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (F/M): ').strip().lower())

    somaIdade += idade
    if sexo == 'm':
        if idade > homemMaisVelhoIdade:
            homemMaisVelhoNome = nome
            homemMaisVelhoIdade = idade
    elif sexo == 'f':
        if idade < 20:
            count += 1

print("""
A média da idade do grupo é {} anos.
O nome do homem mais velho é {}.
{} mulher(es) têm menos de 20 anos.
""".format(somaIdade/4, homemMaisVelhoNome.title(), count))