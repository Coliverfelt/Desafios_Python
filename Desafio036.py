# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Insira o valor da casa: R$'))
salarioComprador = float(input('Insira o salário do comprador: R$'))
anos = int(input('Em quantos anos ele pretende pagar?\n'))

qtdMeses = anos * 12
trintaPorCentoSalario = salarioComprador * 0.3

prestacaoMensal = valorCasa/qtdMeses

if prestacaoMensal > trintaPorCentoSalario:
    print('Empréstimo negado!')
    print('O valor da prestação mensal é {} e excede R${:.2f} de 30% do seu salário (R${:.2f}).'.format(prestacaoMensal, prestacaoMensal-trintaPorCentoSalario, trintaPorCentoSalario))
else:
    print('Empréstimo aprovado!')
    print('Para pagar uma casa de R${:.2f} em {} anos'.format(valorCasa, anos), end = ' ')
    print('será necessário pagar uma prestação de R${:.2f} em {} meses.'.format(prestacaoMensal, qtdMeses))
    print('{}OBSERVAÇÃO!!{}\n30% do seu salário é R${:.2f}.'.format('\033[1::41m', '\033[m', trintaPorCentoSalario))