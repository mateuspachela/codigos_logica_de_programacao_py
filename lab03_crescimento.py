anos = 0

casos_teste = int(input())
for i in range(1, casos_teste+1):
    dados = input().split()
    populacao_a = int(dados[0])
    populacao_b = int(dados[1])
    crescimento_a = float(dados[2])
    crescimento_b = float(dados[3])
    populacao_total_a = int(populacao_a + (((crescimento_a / 100) * populacao_a) * anos))
    populacao_total_b = int(populacao_b + (((crescimento_b / 100) * populacao_b) * anos))


    while populacao_total_a <= populacao_total_b:
        anos += 1
        if anos <= 100:
            populacao_total_a += ((crescimento_a / 100) * populacao_total_a)
            populacao_total_b += ((crescimento_b / 100) * populacao_total_b)
            populacao_total_a = int(populacao_total_a)
            populacao_total_b = int(populacao_total_b)
        else:
            break
    if anos > 100:
        print('Mais de 1 seculo.')
    else:
        print(f'{anos} anos.')
    anos = 0