# 8 - jogadas do jogador
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota) 

lista_linha_coluna_ataque_oponente_anterior = []
lista_linha_coluna_ataque_anterior = []
jogando = True
while jogando:
    def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '___________      ___________\n'
        
        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
            
        return texto
    
    print (monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    linha_coluna_invalida = True
    while linha_coluna_invalida:

        linha_invalida = True

        while linha_invalida:
            linha_atacar = int(input('Linha de ataque: '))
            if linha_atacar > 9 or linha_atacar < 0:
                print ('Linha inválida!')
                
            else:
                linha_invalida = False
        
        coluna_invalida = True
    
        while coluna_invalida:
            coluna_atacar = int(input('Coluna de ataque: '))
            if coluna_atacar > 9 or coluna_atacar < 0:
                print ('Coluna inválida!')
                
            else:
                coluna_invalida = False
        
        lista_linha_coluna_ataque = [linha_atacar]
        lista_linha_coluna_ataque. append(coluna_atacar)
        
        if lista_linha_coluna_ataque in lista_linha_coluna_ataque_anterior:
            print ('A posição linha {0} e coluna {1} já foi informada anteriormente!'.format(linha_atacar, coluna_atacar))
            
        else:
            lista_linha_coluna_ataque_anterior.append(lista_linha_coluna_ataque)
            linha_coluna_invalida = False

    novo_tabuleiro = faz_jogada(tabuleiro_oponente, linha_atacar, coluna_atacar)
    quantos_afundados = afundados (frota_oponente, novo_tabuleiro)

    if quantos_afundados == 10:
        print ('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False

# jogadas do oponente
    linha_coluna_oponente_invalida = True
    while linha_coluna_oponente_invalida:
        linha_ataque_oponente = random.randint(0,9)
        coluna_ataque_oponente = random.randint(0,9)
        
        lista_linha_coluna_ataque_oponente = [linha_ataque_oponente, coluna_ataque_oponente]
        
        if lista_linha_coluna_ataque_oponente not in lista_linha_coluna_ataque_oponente_anterior:
            lista_linha_coluna_ataque_oponente_anterior.append(lista_linha_coluna_ataque_oponente)
            linha_coluna_oponente_invalida = False
            print('Seu oponente está atacando na linha {0} e coluna {1}'.format(linha_ataque_oponente, coluna_ataque_oponente))
            novo_tabuleiro = faz_jogada(tabuleiro_jogador, linha_ataque_oponente, coluna_ataque_oponente)
            quantos_afundados = afundados (frota, novo_tabuleiro)

    if quantos_afundados == 10:
        print ('Xi! O oponente derrubou toda a sua frota =(')
        jogando = False