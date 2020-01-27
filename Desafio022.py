# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).


nome = input('Digite seu nome completo: ').strip()

print('Seu nome em MAIÚSCULAS é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))

#qtdletras = len(nome.replace(" ", ""))
#print('Seu nome tem {} letras.'.format(qtdletras))
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))

splitnome = nome.split()
print(splitnome)
print('Seu primeiro nome é {} e possui {} letras.'.format(splitnome[0], len(splitnome[0])))
print('Seu nome tem {} letras.'.format(len(splitnome[0]) + len(splitnome[1]) + len(splitnome[2]) + len(splitnome[3]) + len(splitnome[4])))
#print('Seu primeiro nome é possui {} letras.'.format(nome.find(" ")))