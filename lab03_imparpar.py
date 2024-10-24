valores = int(input()) # valores que serão lidos

for i in range (1, valores + 1):
    entrada_i = int(input())
    if entrada_i == 0:
        print('NULL')
    elif entrada_i > 0 and entrada_i % 2 == 0:
        print('EVEN POSITIVE')
    elif entrada_i > 0 and (entrada_i % 2 != 0):
        print('ODD POSITIVE')
    elif entrada_i < 0 and entrada_i % 2 == 0:
        print('EVEN NEGATIVE')
    elif entrada_i < 0 and entrada_i % 2 != 0:
        print('ODD NEGATIVE')