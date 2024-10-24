notas = [100, 50, 20, 10, 5, 2, 1]
valor = int(input())
print(valor)
soma_das_notas = []

for i in range(0, 7):
    nota = notas[i]
    quantidade_notas = valor // nota
    valor -= nota * quantidade_notas
    soma_das_notas.append(quantidade_notas)
    print(f'{soma_das_notas[i]} nota(s) de R$ {notas[i]},00')