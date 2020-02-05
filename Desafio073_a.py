# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

rankingBrasileirao = ('Palmeiras', 'Cruzeiro', 'Grêmio', 'Santos', 'Corinthians', 'Flamengo', 'Atlético Mineiro',
                      'Athletico Paranaense', 'Internacional', 'Chapecoense', 'Botafogo', 'São Paulo', 'Fluminense',
                      'Vasco da Gama', 'Bahia', 'Sport', 'Vitória', 'Ponte Preta', 'América', 'Coritiba')
print('*' * 40)
print(f'\033[1:34mOS PRIMEIROS\033[m \033[7m 5 \033[m\033[1:34m COLOCADOS DO BRASILEIRÃO 2019:\033[m')
for posicao in range(0, 5):
    print(f'\033[1:33m{posicao + 1}°\033[m \033[1:34mlugar:\033[m {rankingBrasileirao[posicao]}')
print('*' * 40)

print('*' * 40)
print(f'\033[1:34mOS ÚLTIMOS\033[m \033[7m 4 \033[m \033[1:34mCOLOCADOS DA TABELA:\033[m')
for posicao in range(19, 15, -1):
    print(f'\033[1:33m{posicao + 1}°\033[m \033[1:34mlugar:\033[m {rankingBrasileirao[posicao]}')
print('*' * 40)

print('*' * 40)
print(f'\033[1:34mORDEM ALFABÉTICA:\033[m')
print(f'\033[1:33m{sorted(rankingBrasileirao)} \033[m')
for i, time in enumerate(rankingBrasileirao):
    print(f'\033[1:33m{sorted(rankingBrasileirao)[i]} \033[m')
print('*' * 40)

print('*' * 40)
print(f'\033[1:34mO time da Chapecoense está na\033[m', end=' ')
print(f'\033[1:33m{rankingBrasileirao.index("Chapecoense") + 1}ª\033[m\033[1:34m posição.\033[m')
print('*' * 40)