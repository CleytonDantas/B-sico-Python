"""Módulo de funções - aula 107"""

def aumentar(p, por=1):
    aumento = p + (p * por / 100)
    return aumento

def diminuir(p, por=1):
    reduzir = p - (p * por / 100)
    return reduzir


def dobro(p):
    return p * 2


def metade(p):
    return p / 2