while True:
    try:
        entrada = input().split()

        num_habitantes = int(entrada[0])
        num_consultas = int(entrada[1])

        notas = []
        consultas = []

        for i in range(num_habitantes):
            nota_cidadao = int(input())
            notas.append(nota_cidadao)

        for j in range(num_consultas):
            consulta = int(input())
            consultas.append(consulta)

        notas.sort(reverse=True)

        for consulta in consultas:
            print(notas[consulta - 1])
    except EOFError:
        break