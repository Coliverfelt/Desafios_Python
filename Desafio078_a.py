lista = list()

for v in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {v}: ')))

print(f'''Lista: {lista}''')
print(f'O MENOR valor {min(lista)} está na(s) posição(ões): ', end='')
for k, v in enumerate(lista):
    if v == min(lista):
        print(f'{k}', end='; ')
print(end='\n')
print(f'O MAIOR valor {max(lista)} está na(s) posição(ões): ', end='')
for k, v in enumerate(lista):
    if v == max(lista):
        print(f'{k}', end='; ')