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

def calcula_pontos_sequencia_baixa(dados):
    tem1 = False
    tem2 = False
    tem3 = False
    tem4 = False
    tem5 = False
    tem6 = False
    
    for d in dados:
        if d == 1:
            tem1 = True
        elif d == 2:
            tem2 = True
        elif d == 3:
            tem3 = True
        elif d == 4:
            tem4 = True
        elif d == 5:
            tem5 = True
        elif d == 6:
            tem6 = True
    
    if (tem1 and tem2 and tem3 and tem4) or \
       (tem2 and tem3 and tem4 and tem5) or \
       (tem3 and tem4 and tem5 and tem6):
        return 15
    
    return 0

def calcula_pontos_sequencia_alta(dados):
    tem1 = False
    tem2 = False
    tem3 = False
    tem4 = False
    tem5 = False
    tem6 = False
    
    for d in dados:
        if d == 1:
            tem1 = True
        elif d == 2:
            tem2 = True
        elif d == 3:
            tem3 = True
        elif d == 4:
            tem4 = True
        elif d == 5:
            tem5 = True
        elif d == 6:
            tem6 = True
    
    if (tem1 and tem2 and tem3 and tem4 and tem5) or \
       (tem2 and tem3 and tem4 and tem5 and tem6):
        return 30
    
    return 0