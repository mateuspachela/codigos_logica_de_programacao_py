numero_testes = int(input())

for teste in range(numero_testes):
    entradas = [input() for j in range(3)]
    dieta = list(entradas[0])
    cafe_da_manha = list(entradas[1])
    almoco = list(entradas[2])
    janta = []    
    alimentos_ingeridos = cafe_da_manha + almoco

    cheater = False

    for alimento in alimentos_ingeridos:
        if alimento not in dieta:
            print('CHEATER')
            cheater = True
            break
        dieta.remove(alimento)
    


    if not cheater:
        dieta.sort()
        janta = ''.join(dieta)
        print(janta) 