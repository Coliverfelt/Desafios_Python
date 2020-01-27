# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

segmentoReta1 = float(input('Comprimeto do segmento de reta 1: '))
segmentoReta2 = float(input('Comprimeto do segmento de reta 2: '))
segmentoReta3 = float(input('Comprimeto do segmento de reta 3: '))

if ((segmentoReta1 + segmentoReta2 > segmentoReta3) and
    (segmentoReta1 + segmentoReta3 > segmentoReta2) and
    (segmentoReta2 + segmentoReta3 > segmentoReta1)):

    print('Esses segmentos podem formar um triângulo...')
    if (segmentoReta1 == segmentoReta2 == segmentoReta3):
        print('EQUILÁTERO!')
    elif ((segmentoReta1 == segmentoReta2) or (segmentoReta1 == segmentoReta3) or (segmentoReta2 == segmentoReta3)):
        print('ISÓSCELES!')
    elif (segmentoReta1 != segmentoReta2 != segmentoReta3 != segmentoReta1): #else:
        print('ESCALENO!')
else:
    print('Esses segmentos não podem formar um triângulo!')