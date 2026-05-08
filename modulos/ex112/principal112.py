"""Adpatar o 108 - Módulos
- Criar um parâmetro que dê a opção de formatar a moeda ou não, para tirar a chamada moeda.moeda..."""

# import moeda # importando o módulo de funções que criei
from ex112.utilidadesCeV import moeda # Posso mostrar ex111 (pasta principal) e 'utilidadesCeV' (pacote)
from ex112.utilidadesCeV import dado

preco = dado.leiadinheiro()
moeda.resumo(preco, 80, 35)
