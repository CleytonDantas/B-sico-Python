"""Módulo de funções - aula 107"""

def aumentar(p, por=1, formato=False):
    aumento = p + (p * por / 100)
    if formato:
        aumento = moeda(aumento)
    return aumento

def diminuir(p, por=1, formato=False):
    reduzir = p - (p * por / 100)
    if formato:
        reduzir = moeda(reduzir)
    return reduzir


def dobro(p, formato=False):
    dob = p * 2
    if formato:
        dob = moeda(dob)
    return dob


def metade(p, formato=False):
    met = float(p / 2)
    if formato:
        met = moeda(met)
    return met

def moeda(p):
    dinheiro = (f'R$ {p:.2f}'.replace('.', ','))
    return dinheiro
