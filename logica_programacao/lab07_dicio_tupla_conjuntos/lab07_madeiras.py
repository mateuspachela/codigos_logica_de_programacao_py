numero_testes = int(input())
linha_vazia = input()

for caso in range(numero_testes):
    total_arvores = 0
    especies_arvores = {}
    ultimo_caso = numero_testes - 1
    while True:
        try:
            especie = input()
            if especie == "":
                break
            else:
                total_arvores += 1
                especies_arvores[especie] = especies_arvores.get(especie, 0) + 1
        except EOFError:
            break
    for especie, contagem in sorted(especies_arvores.items()):
        porcentagem = (contagem / total_arvores) * 100
        print(f"{especie} {porcentagem:.4f}")
    if caso != ultimo_caso:
        print('')