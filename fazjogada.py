def faz_jogada(tabuleiro, linha, coluna):
    posicao = tabuleiro[linha][coluna]

    if posicao == 1:
        tabuleiro[linha][coluna] = 'X'

    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro
