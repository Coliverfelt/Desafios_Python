# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("""
         As retas R1 = {:.2f}cm
                  R2 = {:.2f}cm
                  R3 = {:.2f}cm
         podem formar um triângulo.
         """.format(r1, r2, r3))
else:
    print("""
        As retas R1 = {:.2f}cm
                 R2 = {:.2f}cm
                 R3 = {:.2f}cm
        NÃO podem formar um triângulo.
        """.format(r1, r2, r3))