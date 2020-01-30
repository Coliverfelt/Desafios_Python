# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maiorIdade = masculino = feminino = menos20 = 0
while True:
    sexo = ' '
    continua = ' '
    idade = int(input('Digite sua idade: '))
    while sexo not in 'fm':
        sexo = str(input('Qual seu sexo? [F|M]')).strip().lower()[0]
    if idade > 18:
        maiorIdade += 1
    if sexo == 'm':
        masculino += 1
    if sexo == 'f' and idade < 20:
        menos20 += 1
    while continua not in 'sn':
        continua = str(input('Você deseja continuar? [S|N]')).strip().lower()[0]
    if continua == 'n':
        break
print(f'''
Você cadastrou {maiorIdade} pessoas com mais de 18 anos.
{masculino} homens foram cadastrados.
{menos20} mulheres tem menos de 20 anos.
''')