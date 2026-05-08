"""Adpatar o 108 - Módulos
- Criar um parâmetro que dê a opção de formatar a moeda ou não, para tirar a chamada moeda.moeda..."""

# import moeda # importando o módulo de funções que criei
from utilidadesCeV import moeda # Posso mostrar ex111 (pasta principal) e 'utilidadesCeV' (pacote)

preco = float(input('Digite o preço (R$): '))
moeda.resumo(preco, 80, 35)
