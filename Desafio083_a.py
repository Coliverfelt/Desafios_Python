# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

lista = list()

expressao = str(input('Digite uma expressão: '))
lista.append(expressao)

contA = contF = parenteses = 0
for i in range(0, len(expressao)):
    print(f'{i}: {lista[0][i]}')
    if lista[0][0] == ')':
        parenteses = -1
    elif lista[0][len(expressao) - 1] == '(':
        parenteses = -1
    elif lista[0][i] == '(':
        contA += 1
        if (lista[0][i + 1] == ')'):
            parenteses = -1
for j in range(len(expressao) - 1, -1, -1):
    if lista[0][j] == '(':
        parenteses = -1
    if lista[0][j] == ')':
        contF += 1
        if lista[0][j - 1] == '(':
            parenteses = -1
if (parenteses == -1) or (contA != contF):
    print('A expressão não é válida!')
else:
    print('A expressão é válida!')
























