# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('aprender',
            'programar',
            'linguagem',
            'python',
            'curso',
            'gratis',
            'estudar',
            'praticar',
            'trabalhar',
            'mercado',
            'programador',
            'futuro')
i = j = 0
for i in range(0, len(palavras)):
    print(f'Na palavra {palavras[i].upper()} temos ', end='')
    for j in range(0, len(palavras[i])):
        if 'a' in palavras[i][j]:
            print(palavras[i][j], end=' ')
        if 'e' in palavras[i][j]:
            print(palavras[i][j], end=' ')
        if 'i' in palavras[i][j]:
            print(palavras[i][j], end=' ')
        if 'o' in palavras[i][j]:
            print(palavras[i][j], end=' ')
        if 'u' in palavras[i][j]:
            print(palavras[i][j], end=' ')
    print(end='\n')
