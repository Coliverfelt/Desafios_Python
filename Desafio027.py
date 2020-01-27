# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome: ').strip()

nome = nome.split()

print(len(nome))
print("""
Primeiro nome: {}
Último nome: {}
""".format(nome[0].title(), nome[len(nome) - 1].title()))