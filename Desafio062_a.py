# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

i = 1

while i <= 10:
    print('{}; '.format(primeiroTermo + (i - 1) * razao), end='')
    i += 1

quantidadeTermos = int(input('\nSe desejar visualizar mais termos digite a quantidade que deseja, senão, digite 0: '))

while quantidadeTermos > 0:
    j = 1
    while j <= quantidadeTermos:
        print('{}; '.format(primeiroTermo + (i - 1) * razao), end='')
        i += 1
        j += 1
    quantidadeTermos = int(input('\nSe desejar visualizar mais termos digite a quantidade que deseja, senão, digite 0: '))

print('Ok, Tchau!')
exit()