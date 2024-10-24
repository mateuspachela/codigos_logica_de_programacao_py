notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
valor = float(input())
soma_das_notas = []
soma_das_moedas = []

print("NOTAS:")
for i in range(0, 6):
    nota = notas[i]
    quantidade_notas = valor // nota
    valor -= nota * quantidade_notas
    soma_das_notas.append(quantidade_notas)
    print(f'{int(soma_das_notas[i])} nota(s) de R$ {notas[i]}.00')
    
valor *= 100
print("MOEDAS:")
for i in range(0, 6):    
    moeda = moedas[i]
    quantidade_moedas = valor // (moeda * 100)
    valor -= (moeda * 100) * quantidade_moedas
    soma_das_moedas.append(quantidade_moedas)
    print(f'{int(soma_das_moedas[i])} moeda(s) de R$ {moedas[i]:.2f}')   