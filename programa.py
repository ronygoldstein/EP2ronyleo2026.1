from funcoes import *

def jogo():
    cartela = {
        'regra_simples': {1:-1,2:-1,3:-1,4:-1,5:-1,6:-1},
        'regra_avancada': {
            'sem_combinacao':-1,
            'quadra':-1,
            'full_house':-1,
            'sequencia_baixa':-1,
            'sequencia_alta':-1,
            'cinco_iguais':-1
        }
    }

    for _ in range(12):
        dados_guardados = []
        dados_rolados = rolar(dados_guardados)
        rerrolagens = 0

        while True:
            print("Dados rolados:", dados_rolados)
            print("Dados guardados:", dados_guardados)
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            
            opcao = input()

            if opcao == "1":
                print("Digite o índice do dado a ser guardado (0 a 4):")
                i = int(input())
                if i >= 0 and i < len(dados_rolados):
                    res = guardar_dado(dados_rolados, dados_guardados, i)
                    dados_rolados = res[0]
                    dados_guardados = res[1]

            elif opcao == "2":
                print("Digite o índice do dado a ser removido (0 a 4):")
                i = int(input())
                if i >= 0 and i < len(dados_guardados):
                    res = remover_dado(dados_rolados, dados_guardados, i)
                    dados_rolados = res[0]
                    dados_guardados = res[1]

            elif opcao == "3":
                if rerrolagens >= 2:
                    print("Você já usou todas as rerrolagens.")
                else:
                    dados_rolados = rolar(dados_guardados)
                    rerrolagens += 1

            elif opcao == "4":
                imprime_cartela(cartela)

            elif opcao == "0":
                print("Digite a combinação desejada:")
                cat = input()

                antes = str(cartela)
                cartela = faz_jogada(dados_rolados + dados_guardados, cat, cartela)

                if str(cartela) == antes:
                    if (cat in cartela['regra_avancada'] and cartela['regra_avancada'][cat] != -1) or \
                       (cat in ["1","2","3","4","5","6"] and cartela['regra_simples'][int(cat)] != -1):
                        print("Essa combinação já foi utilizada.")
                    else:
                        print("Combinação inválida. Tente novamente.")
                    continue

                break

            else:
                print("Opção inválida. Tente novamente.")

    imprime_cartela(cartela)

    total = 0

    for v in cartela['regra_simples'].values():
        if v != -1:
            total += v

    for v in cartela['regra_avancada'].values():
        if v != -1:
            total += v

    soma_simples = 0
    for v in cartela['regra_simples'].values():
        if v != -1:
            soma_simples += v

    if soma_simples >= 63:
        total += 35

    print("Pontuação total:", total)


jogo()