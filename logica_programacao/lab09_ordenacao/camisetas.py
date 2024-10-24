#lab9.3
contador = False # variavel booleana para evitar print a mais no ultimo caso
while True: # enquanto houver numero de camisetas para testar
    qtd_camisetas = int(input()) # entrada do usuario de quantas camisetas serao

    if qtd_camisetas == 0: # se for zero ele para de executar o programa
        break

    else: # se nao ele executa o programa
        lista_informacoes = [] # lista que recebe as informacoes de cada camiseta
        for camiseta in range(qtd_camisetas): # loop que preenche a lista com as informacoes
            nome = str(input())
            cor, tamanho = input().split()
            lista_informacoes.append((cor, tamanho, nome))

        lista_informacoes.sort(key=lambda x: (x[0], -ord(x[1]), x[2])) # metodo de ordenacao que olhará primeiramente a cor, depois o tamanho, e por fim o nome, assim ordenando na ordem solicitada do exercicio, olhara o tamanho calculando seu valor na tabela asc mas de forma indireta, ja que p tem maior valor que m e g, porem nesse caso ele deve ser  menor valor
        if contador:
            print('')
        for informacao in lista_informacoes: # loop para printar de acordo com o que foi pedido
            print(informacao[0], informacao[1], informacao[2])
        contador = True