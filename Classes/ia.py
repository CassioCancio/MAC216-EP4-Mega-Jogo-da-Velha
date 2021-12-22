from tabuleiro import Tabuleiro
from jogador import Jogador
from mega_tabuleiro import MegaTabuleiro
from random import randint
from Modulos.auxiliar import ind_pos

class IA(Jogador):
    def __init__(self, nome, simbolo):
        Jogador.__init__(self, nome, simbolo)

    def preparar_jogada(self, tabuleiro:MegaTabuleiro):
        self.esperar()
        linha = coluna = sub_linha = sub_coluna = id = id_rival = None
        # Define id do jogador atual e de seu rival
        if(self.simbolo == 'x'):
            id = 0
            id_rival = 1
        else:
            id = 1
            id_rival = 0

        # Encontra o subtabuleiro correto
        for indice in range(0, 9):
            i, j = ind_pos(indice)
            if(tabuleiro.ha_subtab(i, j) and tabuleiro.conta_jogadas(i, j, id)):
                linha = i
                coluna = j
                break

        # Se não encontrar tabuleiro correto, joga no primeiro disponível
        if(linha == None):
            for indice in range(9):
                i, j = ind_pos(indice)
                if(tabuleiro.ha_subtab(i, j)):
                    linha = i
                    coluna = j
                    break

        sub_tabuleiro = tabuleiro.receber_posicao(linha, coluna)
                        
        # Se não houver jogada no meio, jogue nessa posição
        posicao_central = tabuleiro.receber_sub_posicao(linha, coluna, 1, 1)
        if(posicao_central == -1):
            return linha, coluna, 1, 1

        # Se o adversário jogar nos cantos centrais ou no meio jogue nas diagonais ou no canto central oposto
        canto_esquerdo_meio = tabuleiro.receber_sub_posicao(linha, coluna, 1, 0)
        canto_cima_meio = tabuleiro.receber_sub_posicao(linha, coluna, 0, 1)
        canto_direito_meio = tabuleiro.receber_sub_posicao(linha, coluna, 1, 2)
        canto_baixo_meio = tabuleiro.receber_sub_posicao(linha, coluna, 2, 1)
        if(canto_baixo_meio == id_rival or canto_cima_meio == id_rival\
            or canto_direito_meio == id_rival or canto_esquerdo_meio == id_rival or posicao_central == id_rival):
            if(tabuleiro.receber_sub_posicao(linha, coluna, 0, 0) == -1):
                return linha, coluna, 0, 0
            elif(tabuleiro.receber_sub_posicao(linha, coluna, 0, 2) == -1):
                return linha, coluna, 0, 2
            elif(tabuleiro.receber_sub_posicao(linha, coluna, 2, 0) == -1):
                return linha, coluna, 2, 0
            elif(tabuleiro.receber_sub_posicao(linha, coluna, 2, 2) == -1):
                return linha, coluna, 2, 2

        # Se não achar posição válida, sorteia uma
        pos_indices = list(range(9))
        for i in range(9):
            sorte = randint(i, 8)
            sub_linha, sub_coluna = ind_pos(pos_indices[sorte])
            if(sub_tabuleiro.verificar_posicao(sub_linha, sub_coluna)): break
            pos_indices[i], pos_indices[sorte] = pos_indices[sorte], pos_indices[i]

        
        return linha, coluna, sub_linha, sub_coluna