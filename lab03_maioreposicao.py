valores = []

for i in range(1, 101):
    valor = int(input())
    valores.append(valor)

maior_valor = max(valores)
print(maior_valor)
print(valores.index(max(valores)) + 1)