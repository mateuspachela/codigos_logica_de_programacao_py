numero_n = int(input())

for i in range (1, 10001):
    numero_dividido = i % numero_n
    if numero_dividido == 2:
        print(i)