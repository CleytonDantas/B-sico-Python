"""Módulo de dinheiro
- Módulo moeda.py: aumentar, diminuir, dobro, metade
- Fazer um programa que importe o modulo e use as funções"""

import moeda # importando o módulo de funções que criei
# from ex107 import moeda - Faz a mesma importação só em 'moeda'

preco = float(input('Digite o preço (R$): '))
print(f'A metade de {preco} é {moeda.metade(preco)}.')
print(f'O dobro de {preco} é {moeda.dobro(preco)}.')
print(f'Aumentando 10%, temos: {moeda.aumentar(preco, 10):.2f}.')
print(f'Reduzindo 13%, temos: {moeda.diminuir(preco, 13):.2f}.')

