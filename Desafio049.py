# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

n = int(input('Digite um número: '))

print('Tabuada de {}:'.format(n))

print('-' * 12)
for i in range(0, 11):
    print('{:2} * {} = {:2}'.format(i, n, i*n))
print('-' * 12)