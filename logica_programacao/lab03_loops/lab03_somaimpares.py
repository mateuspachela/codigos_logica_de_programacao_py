numero_um = int(input())
numero_dois = int(input())
soma = 0
for numero in range(numero_dois+1, numero_um):
    if (numero % 2 != 0):
        soma += numero
print(soma)