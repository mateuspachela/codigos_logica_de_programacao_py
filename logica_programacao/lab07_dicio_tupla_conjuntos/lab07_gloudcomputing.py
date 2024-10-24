while True:
    servidores_clientes = input().split()
    numero_servidores = int(servidores_clientes[0])
    numero_clientes = int(servidores_clientes[1])

    if numero_servidores == 0 and numero_clientes == 0:
        break

    servidores = []
    clientes = []
    conexoes = 0

    for servidor in range(numero_servidores):
         numero_aplicacoes_servidor = input().split()
         numero_requisicoes_servidor = int(numero_aplicacoes_servidor[0])
         aplicacoes = set(numero_aplicacoes_servidor[1:])
         servidores.append(aplicacoes)

    for cliente in range(numero_clientes):
        numero_aplicacoes_cliente = input().split()
        numero_requisicoes_cliente = int(numero_aplicacoes_cliente[0])
        requisicoes = set(numero_aplicacoes_cliente[1:])
        clientes.append(requisicoes)
    
    for cliente in clientes:
        for servidor in servidores:
            if cliente & servidor:
                conexoes += 1
    
    print(conexoes)