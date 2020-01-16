# Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Temperatura °C: '))
fahrenheit = (1.8 * celsius) + 32

print('A temperatura em Fahrenheit é {}°F.'.format(fahrenheit))
