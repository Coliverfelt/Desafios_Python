# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

i = 1
maisTermos = 10
total = 0

while maisTermos != 0:
    total += maisTermos
    while i <= total:
        print('{}; '.format(primeiroTermo + (i - 1) * razao), end='')
        i += 1
    maisTermos = int(input('\nSe desejar visualizar mais termos digite a quantidade que deseja, senão, digite 0: '))
print('Progressão finalizada com {} termos.'.format(total))