import numpy as np
from jogador import Jogador
from mega_tabuleiro import MegaTabuleiro

class Estabanado(Jogador):
    def __init__(self):
        Jogador.__init__()

    def preparar_jogada(self, tabuleiro: MegaTabuleiro):
        # Sorteando tabuleiro livre
        sub_tabuleiro = None
        sub_tabuleiros = [0,1,2,3,4,5,6,7,8]
        linha = None
        coluna = None
        for i in range(9):
            indice = np.random.randint(low=i, high=9)
            coluna = indice % 3
            linha = (indice - coluna) // 3
            if(tabuleiro.verificar_posicao(linha, coluna)):
                sub_tabuleiro = tabuleiro.posicoes[indice]
                break
            sub_tabuleiros[i], sub_tabuleiros[indice] = sub_tabuleiros[indice], sub_tabuleiros[i]

        # Sorteando posição livre no tabuleiro
        posicao = None
        posicoes = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        linha_sub = None
        coluna_sub = None
        for i in range(9):
            indice = np.random.randint(low=i, high=9)
            coluna_sub = indice % 3
            linha_sub = (indice - coluna) // 3
            if(sub_tabuleiro.verificar_posicao(linha, coluna)):
                break
            posicoes[i], posicoes[indice] = posicoes[indice], posicoes[i]

        # Se não achar posição disponível
        if sub_tabuleiro == None:
            pass #toDo

        # Retorna o subtabuleiro escolhido e a posição escolhida para a jogada
        return sub_tabuleiro, linha_sub, coluna_sub