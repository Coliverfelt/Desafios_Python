# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

cores = {'limpa': '\033[m',
         'negamarelo': '\033[1:33m',
         'negazul': '\033[1:34m',
         'peb': '\033[7m'}

valorProduto = float(input('Valor do produto R$'))

print('\n')
print(('{}={}{}-{}{}={}'.format(cores['negamarelo'], cores['limpa'],
                                cores['negazul'], cores['limpa'],
                                cores['negamarelo'], cores['limpa']) * 7), end = '')

print('{}{}{}'.format(cores['peb'], 'FORMAS DE PAGAMENTO', cores['limpa']), end = '')

print('{}={}{}-{}{}={}'.format(cores['negamarelo'], cores['limpa'],
                               cores['negazul'], cores['limpa'],
                               cores['negamarelo'], cores['limpa']) * 7)

print('''
    {}1{} {}-{} Dinheiro/Cheque (À vista: 10% de desconto)
    {}2{} {}-{} Cartão (À vista: 5% de desconto)
    {}3{} {}-{} Cartão (Em até 2x: Sem juros)
    {}4{} {}-{} Cartão (A partir de 3x: 20% de juros)
       '''.format(cores['negamarelo'], cores['limpa'],
                  cores['negazul'], cores['limpa'],
                  cores['negamarelo'], cores['limpa'],
                  cores['negazul'], cores['limpa'],
                  cores['negamarelo'], cores['limpa'],
                  cores['negazul'], cores['limpa'],
                  cores['negamarelo'], cores['limpa'],
                  cores['negazul'], cores['limpa']))

print('{}={}{}-{}{}={}'.format(cores['negamarelo'], cores['limpa'],
                                cores['negazul'], cores['limpa'],
                                cores['negamarelo'], cores['limpa']) * 20)

formaPagamento = int(input())

if formaPagamento == 1:
    print('O valor final do produto será R${}.'.format(valorProduto - (valorProduto * 0.1)))
elif formaPagamento == 2:
    print('O valor final do produto será R${}.'.format(valorProduto - (valorProduto * 0.05)))
elif formaPagamento == 3:
    print('O valor final do produto será R${}'.format(valorProduto), end = '')
    print(', e caso parcele em até 2x, cada parcela sairá no valor de R${} SEM JUROS.'.format(valorProduto // 2))
elif formaPagamento == 4:
    qtdParcela = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(qtdParcela, (valorProduto + (valorProduto * 0.2)) / qtdParcela))
    print('O valor final do produto será R${}.'.format(valorProduto + (valorProduto * 0.2)))