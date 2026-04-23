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

def calcula_pontos_regra_simples(dados):
    resultado = {}
    for i in range(1, 7):
        soma = 0
        for dado in dados:
            if dado == i:
                soma += i
        resultado[i] = soma
    return resultado

def calcula_pontos_soma(dados):
    soma = 0
    for dado in dados:
        soma += dado
    return soma