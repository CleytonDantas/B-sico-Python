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

def resumo(p, aum=1, red=1):
    print('-' * 30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('-' * 30)
    print(f'{'Preço analisado:':<16} {moeda(p,):>12}')
    print(f'{'Dobro do Preço:':<16} {dobro(p, True):>12}')
    print(f'{'Metade do Preço:':<16} {metade(p, True):>12}')
    print(f'{'80% de aumento:':<16} {aumentar(p, aum, True):>12}')
    print(f'{'35% de redução:':<16} {diminuir(p, red, True):>12}')
    print('-' * 30)