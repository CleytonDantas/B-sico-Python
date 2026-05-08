

def leiadinheiro():
    while True:
        valor = input('Digite o preço (R$): ').replace(',', '.').strip()
        print(valor.isalpha(), valor.isnumeric())
        if valor.isalpha() or not valor:
            print('\033[0;31mDado inválido!\033[m')
        else:
            valor = float(valor)
            return valor
            break

