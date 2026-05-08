"""Adpatar o 108 - Módulos
- Criar um parâmetro que dê a opção de formatar a moeda ou não, para tirar a chamada moeda.moeda..."""

# import moeda # importando o módulo de funções que criei
from ex110 import moeda

preco = float(input('Digite o preço (R$): '))
moeda.resumo(preco, 80, 35)
