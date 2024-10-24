numero_n = int(input())
peso_um = 2
peso_dois = 3
peso_tres = 5
soma_pesos = peso_um + peso_dois + peso_tres

for i in range (1, numero_n+1):
    numero_um, numero_dois, numero_tres = input().split()
    numero_um = float(numero_um)
    numero_dois = float(numero_dois)
    numero_tres = float(numero_tres)
    media = ((peso_um * numero_um) + (peso_dois * numero_dois) + (peso_tres * numero_tres))/ soma_pesos
    print(f'{media:.1f}')