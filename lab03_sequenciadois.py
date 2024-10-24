numero_um, numero_dois = input().split()
numero_um = int(numero_um)
numero_dois = int(numero_dois)
auxiliar = 1

for i in range (1, numero_dois + 1):
    if (auxiliar != numero_um):
        print(i, end=" ")
        auxiliar += 1
    else:
        print(i)
        auxiliar = 1