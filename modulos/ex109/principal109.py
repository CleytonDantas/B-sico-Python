"""Adpatar o 108 - Módulos
- Criar um parâmetro que dê a opção de formatar a moeda ou não, para tirar a chamada moeda.moeda..."""

# import moeda # importando o módulo de funções que criei
from ex109 import moeda # Faz a mesma importação só em 'moeda'

preco = float(input('Digite o preço (R$): '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}.')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}.')
print(f'Aumentando 10%, temos: {moeda.aumentar(preco, 10, True)}.')
print(f'Reduzindo 13%, temos: {moeda.diminuir(preco, 13, True)}.')
