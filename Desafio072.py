# Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numerosExtenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
                  'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
                  'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
                  'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    numero = int(input('Digite um número de 0 a 20: '))
    if 0 <= numero <= 20:
        print(f'Você digitou o número {numerosExtenso[numero]}.')
        continuar = str(input('Deseja continuar? [S/N]')).lower().strip()[0]
        while continuar not in 'sn':
            continuar = str(input('Favor digitar apenas S ou N. Deseja continuar? [S/N]')).lower().strip()[0]
        if continuar in 'n':
            break