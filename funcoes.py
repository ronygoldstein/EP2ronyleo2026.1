import random

def rolar_dados(qtd):
    resultados = []
    for _ in range(qtd):
        resultados.append(random.randint(1, 6))
    return resultados