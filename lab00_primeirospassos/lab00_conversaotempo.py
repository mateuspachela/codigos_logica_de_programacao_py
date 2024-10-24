tempo_duracao = int(input())
segundos = 0
minutos = 0
horas = 0

if tempo_duracao >= 60:
    minutos = tempo_duracao // 60
    segundos = tempo_duracao % 60
    if minutos >= 60:
        horas = minutos // 60
        minutos %= 60
else:
    segundos = tempo_duracao
    
print(f'{horas}:{minutos}:{segundos}')