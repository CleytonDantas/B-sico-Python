"""Módulos e Pacotes"""

"""Vantagens:
- Organização do código
- Facilidade de manutenção
- Ocultação de código detalhado
- Reutilização em outros projetos
"""

from uteis import numeros
# from uteis import * # isso importa tudo do módulo 'numeros' dentro do pacote 'uteis'

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num) # numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {numeros.dobro(num)}. Já o triplo é {numeros.triplo(num)}.')

"""Pacotes ajudam quando o módulo fica robusto.
- Pacotes são pastas de módulos.
Ex: Tenho um pacote chamado uteis. Dentro dela tenho vários módulos: números, strings, datas, cores, etc
Para importar o pacote é da mesma forma: import uteis / from uteis import datas"""

# Todo arquivo  .py pode ser um módulo
# Toda pasta é considerada um pacote, dentro de um projeto Python.
# Sintaxe para nome de arquivo dentro de pacotes: __init__.py
# Ao criar o pacote (pasta) ele já cria o arquivo __init__.py
