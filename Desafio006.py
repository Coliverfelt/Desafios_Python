# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))

#print('O dobro de {} é {}. \nO triplo de {} é {}. \nA raiz quadrada de {} é {:.2f}.'.format(n, n*2, n, n*3, n, n**(1/2)))
print('O dobro de {} é {}.'.format(n, n*2))
print('O triplo de {} é {}.'.format(n, n*3,))
print('A raiz quadrada de {} é {:.2f}.'.format(n, pow(n, (1/2))))