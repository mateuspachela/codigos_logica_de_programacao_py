# lab 02

onde_jogar = int(input())

if onde_jogar == 0: # Jogos físicos
    jogar_com_quem = int(input()) # Usuario deve escolher com quem vai jogar
    if jogar_com_quem == 0: # Familia
        faixa_etaria = int(input()) # Usuario deve escolher a faixa etaria do jogo
        if faixa_etaria == 0: # 4+
            print('O Castelo é Nosso')
        elif faixa_etaria == 1: # 10+
            print('Mysterium Park')
        elif faixa_etaria == 2: # 14+
            print('Pandemic')
        else: # 18+
            print('Qual É o Seu Meme?')
    elif jogar_com_quem == 1: # Galera
        max_participantes = int(input()) # Usuario deve digitar quantidade de participantes máxima
        if max_participantes == 0: # 4 Participantes
            print('Descent: Lendas da Escuridão')
        elif max_participantes == 1: # 7 Participantes
            print('Dixit')
        elif max_participantes == 2: # 10 Participantes
            print('The Resistance')
        else: # 16 Participantes
            print('Sim, Mestre das Trevas (Edição Verde)')
    elif jogar_com_quem == 2: # Crianças
        intevalo_preco = int(input()) # Usuario deve digitar o intervalo de preço do jogo a ser recomendado
        if intevalo_preco == 0: # de R$ 0 até 99,99
            print('Dobble: Pixar')
        elif intevalo_preco == 1: # de R$ 100,00 até 199,99
            print('Caça aos Monstros')
        elif intevalo_preco == 2: # de R$ 200,00 até 299,99
            print('Ticket to Ride: Trem Fantasma')
        else: # de R$ 300 até 399,99
            print('Scooby-Doo: The Board Game')
    else: # A dois
        tempo_partida = int(input()) # Usuario deve digitar o intervalo de tempo para uma partida do jogo a ser recomendado
        if tempo_partida == 0: # 15 minutos
            print('Exploding Kitens')
        elif tempo_partida == 1: # 30 minutos
            print('7 Wonders Duel')
        elif tempo_partida == 2: # 31 a 60 minutos
            print('Azul: Pavilhão de Verão')
        elif tempo_partida == 3: # 61 a 120 minutos
            print('Power Grid: Versão Energizada')
        else: # Mais de 120 minutos
            print('Star Wars Rebellion')
else: # Jogos virtuais
    qual_genero = int(input()) # Usuario deve digitar o genero do jogo a ser recomendado
    if qual_genero == 0: # RPG
        tipo_rpg = int(input())
        if tipo_rpg == 0: # RPG de Aventura
            ano_lancamento = int(input())
            if ano_lancamento == 0: # Lançado em 2021
                print('Valheim')
            elif ano_lancamento == 1: # Lançado em 2022
                print('God of War')
            elif ano_lancamento == 2: # Lançado em 2023
                print("Baldur's Gate 3")
            else: # Lançado em 2024
                print('Palworld')
        elif tipo_rpg == 1: # RPG de Ação
            qual_tematica = int(input()) # Usuario deve digitar a tematica do jogo RPG a ser recomendado
            if qual_tematica == 0: # Temática Pós Apocaliptico
                print('Horizon Forbidden West')
            elif qual_tematica == 1: # Temática Fantasia
                print('Hogwarts Legacy')
            else: # Temática Soulslike
                print('ELDEN RING')
    elif qual_genero == 1: # Esportes
        qual_categoria = int(input()) # Usuario deve digitar o tipo de esporte do jogo a ser recomendado
        if qual_categoria == 0: # Corrida
            print('Forza Horizon 4')
        elif qual_categoria == 1: # Skate
            print('Session: Skate Sim')
        else: # Futebol
            print('FIFA 22')
    elif qual_genero == 2: # Simulador
        qual_tipo = int(input()) # Usuario deve digitar o tipo de jogo de simulador a ser recomendado
        if qual_tipo == 0: # Automobilistico
            print('Euro Truck Simulator 2')
        elif qual_tipo == 1: # Rural
            print('Stardew Valley')
        elif qual_tipo == 2: # Espacial
            print('Kerbal Space Program')
        else: # Vida real
            qual_jogo = int(input()) # Usuario deve escolher uma opção entre os The Sims
            if qual_jogo == 0:
               print('The Sims 1')
            elif qual_jogo == 1:
                print('The Sims 2')
            elif qual_jogo == 2:
                print('The Sims 3')
            else: # The Sims 4
                expansao = int(input()) # Usuario deve escolher uma expansao do The Sims 4
                if expansao == 0:
                    print('Parenthood')
                elif expansao == 1:
                    print('Junte-se à Galera')
                elif expansao == 2:
                    print('Vida Campestre')
                elif expansao == 3:
                    print('A aventura de Crescer')
                elif expansao == 4:
                    print('Vida Universiária')
                else:
                    print('Cats & Dogs')
    elif qual_genero == 3: # Defesa de Torres
        avaliacao_steam = int(input()) # # Usuario deve escolher uma faixa de avaliacoes da Steam
        if avaliacao_steam == 0: # Extremamente positivas
            print('Thronefall')
        elif avaliacao_steam == 1: # Muito positivas
            print('Orcs Must Diel 3')
        elif avaliacao_steam == 2: # Ligeiramente positivas
            print('Plants vs. Zombies')