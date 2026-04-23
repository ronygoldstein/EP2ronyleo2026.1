import random

def rolar_dados(qtd):
    resultados = []
    for _ in range(qtd):
        resultados.append(random.randint(1, 6))
    return resultados

def guardar_dado(dados_rolados, dados_no_estoque, indice):
    dado = dados_rolados[indice]
    del dados_rolados[indice]
    dados_no_estoque.append(dado)
    return [dados_rolados, dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, indice):
    dado = dados_no_estoque[indice]
    del dados_no_estoque[indice]
    dados_rolados.append(dado)
    return [dados_rolados, dados_no_estoque]