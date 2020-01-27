# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.

palavra1 = input('Insira uma palavra: ').strip().lower()

palavra1SemEspaco = palavra1.replace(" ", "")
palavra2 = ""

for i in range(len(palavra1SemEspaco) -1, -1, -1):
    palavra2 += palavra1SemEspaco[i]

if palavra1SemEspaco == palavra2:
    print('É um palíndromo, pois a palavra é igual a ela mesma lida da esquerda pra direita e vice-versa: ')
    print('Palavra: {}'.format(palavra1SemEspaco))
    print('Lendo da direita para a esquerda: {}'.format(palavra2))
else:
    print('Não é um palíndromo, pois a palavra não é igual a ela mesma lida da esquerda pra direita e vice-versa: ')
    print('Palavra: {}'.format(palavra1SemEspaco))
    print('Lendo da direita para a esquerda: {}'.format(palavra2))