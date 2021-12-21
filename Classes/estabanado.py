from random import randint
from jogador import Jogador
from mega_tabuleiro import MegaTabuleiro
from Modulos.auxiliar import ind_pos

class Estabanado(Jogador):
    def __init__(self, nome, simbolo):
        Jogador.__init__(self, nome, simbolo)

    def preparar_jogada(self, tabuleiro: MegaTabuleiro):
        # Sorteando tabuleiro livre
        sub_tabuleiro = None
        sub_tabuleiros = [0,1,2,3,4,5,6,7,8]
        linha = None
        coluna = None
        for i in range(9):
            indice = randint(i, 8)
            linha, coluna = ind_pos(indice)
            if(tabuleiro.verificar_posicao(linha, coluna)):
                sub_tabuleiro = tabuleiro.posicoes[indice]
                break
            sub_tabuleiros[i], sub_tabuleiros[indice] = sub_tabuleiros[indice], sub_tabuleiros[i]

        # Sorteando posição livre no tabuleiro
        posicao = None
        posicoes = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        sub_linha = None
        sub_coluna = None
        for i in range(9):
            indice = randint(i, 8)
            sub_linha, sub_coluna = ind_pos(indice)
            if(sub_tabuleiro.verificar_posicao(sub_coluna, sub_linha)):
                break
            posicoes[i], posicoes[indice] = posicoes[indice], posicoes[i]

        # Retorna o subtabuleiro escolhido e a posição escolhida para a jogada
        return linha, coluna, sub_linha, sub_coluna